from CustomBollingerBand import CustomBollingerBand

import lightgbm as lgb
import numpy as np
import pandas as pd

class SymbolData:
    """
    This class holds all of the data for a security. It's responsible for training the
    gradient boosting model and making predictions. 
    """
    
    def __init__(self, symbol, algorithm, hold_duration, k_start=0.5, k_end=5, 
                 k_step=0.25, training_weeks=4, max_depth=1, num_leaves=2, num_trees=20,
                 commission=0.02, spread_cost=0.03):
        """
        Input:
         - symbol
            Represents a unique security identifier
         - algorithm
            Algorithm instance running the backtest
         - hold_duration
            Number of timesteps ahead to predict
         - k_start
            Starting k for indicator parameter loop
         - k_end
            Ending k for indicator parameter loop
         - k_step
            Stepping k for indicator parameter loop
         - training_weeks
            Number of weeks of historical data to train on
         - max_depth
            Maximum depth of the trees built
         - num_leaves
            Number of leaves for each tree
         - num_trees
            Number of trees to build
         - commission
            Commission cost of trading round-trip
         - spread_cost
            Spread cost of trading round-trip
        """
        self.symbol = symbol
        self.algorithm = algorithm
        self.hold_duration = hold_duration
        self.resolution = algorithm.UniverseSettings.Resolution
        self.training_length = int(training_weeks * 5 * 6.5 * 60) # training_weeks in minutes
        self.max_depth = max_depth
        self.num_leaves = num_leaves
        self.num_trees = num_trees
        self.cost = commission + spread_cost
        
        self.indicator_consolidators = []
    
        # Train a model at the end of each month
        self.model = None
        algorithm.Train(algorithm.DateRules.MonthEnd(symbol), 
                        algorithm.TimeRules.BeforeMarketClose(symbol), 
                        self.train)
        
        # Avoid overnight holds
        self.allow_predictions = False
        self.events = [
            algorithm.Schedule.On(algorithm.DateRules.EveryDay(symbol), 
                                  algorithm.TimeRules.AfterMarketOpen(symbol, 0), 
                                  self.start_predicting),
            algorithm.Schedule.On(algorithm.DateRules.EveryDay(symbol), 
                                  algorithm.TimeRules.BeforeMarketClose(symbol, hold_duration + 1),
                                  self.stop_predicting)
        ]
        
        self.setup_indicators(k_start, k_end, k_step)
        self.train()
        
        
    def setup_indicators(self, k_start, k_end, k_step):
        """
        Initializes all the technical indicators and their historical windows.
        
        Input:
         - k_start
            Starting k for indicator parameter loop
         - k_end
            Ending k for indicator parameter loop
         - k_step
            Stepping k for indicator parameter loop
        """
        self.indicators_by_indicator_type = {}
        self.indicators_history_by_indicator_type = {}
        self.max_warm_up_period = 0
        
        for k in np.arange(k_start, k_end + k_step, k_step):
            indicators = {
                'rsi' : RelativeStrengthIndex(int(14*k)),
                'macd': MovingAverageConvergenceDivergence(int(12*k), int(26*k), 9),
                'bb'  : CustomBollingerBand(int(20*k), 2)
            }
            
            for indicator_type, indicator in indicators.items():
                # Register indicators for automatic updates
                consolidator = self.algorithm.ResolveConsolidator(self.symbol, self.resolution)
                self.algorithm.RegisterIndicator(self.symbol, indicator, consolidator)
                self.indicator_consolidators.append(consolidator)
                
                # Save reference to indicators
                if indicator_type not in self.indicators_by_indicator_type:
                    self.indicators_by_indicator_type[indicator_type] = []
                    self.indicators_history_by_indicator_type[indicator_type] = []
                self.indicators_by_indicator_type[indicator_type].append(indicator)
                
                # Create empty lookback window for indicator history
                self.indicators_history_by_indicator_type[indicator_type].append(np.array([]))
        
                # Find max warmup period
                self.max_warm_up_period = max(self.max_warm_up_period, indicator.WarmUpPeriod)
                
        self.history_length = self.training_length + self.max_warm_up_period
        
    
    def reset_state(self):
        """
        Resets all the technical indicators and their histories.
        """
        for indicator_type, indicators_history in self.indicators_history_by_indicator_type.items():
            self.indicators_history_by_indicator_type[indicator_type] = [np.array([]) for _ in range(len(indicators_history))]
            for indicator in self.indicators_by_indicator_type[indicator_type]:
                indicator.Reset()
        
        
    def train(self):
        """
        Trains the gradient boosting model using indicator values as input and 
        future return as output.
        """
        self.reset_state()
        
        # Request history for indicator warm up
        history = self.algorithm.History(self.symbol, self.history_length, self.resolution)
        if history.empty or history.shape[0] < self.history_length:
            self.algorithm.Log(f"Not enough history for {self.symbol} to train yet.")
            return
        history = history.loc[self.symbol].close
        
        # Warm up indicators and history of indicators
        for indicator_type, indicators in self.indicators_by_indicator_type.items():
            for idx, indicator in enumerate(indicators):
                warm_up_length = self.training_length + indicator.WarmUpPeriod - 1
                warm_up_data = history.iloc[-warm_up_length:]
                for time, close in warm_up_data.iteritems():
                    # Update indicator
                    indicator.Update(time, close)
        
                    # Update indicator history
                    if indicator.IsReady:
                        current_history = self.indicators_history_by_indicator_type[indicator_type][idx]
                        appended = np.append(current_history, indicator.Current.Value)
                        self.indicators_history_by_indicator_type[indicator_type][idx] = appended
        
        history = history.iloc[self.max_warm_up_period:]
        label = history.shift(-self.hold_duration) - history

        
        
        ##################
        ## Clean Training Data
        ##################
        # Remove last `hold_duration` minutes of each day to avoid overnight holdings
        
        # Get clean indices
        data_points_per_day = [len(g) for _, g in label.groupby(pd.Grouper(freq='D')) if g.shape[0] > 0]
        clean_indices = []
        for i in range(len(data_points_per_day)):
            from_index = 0 if i == 0 else data_points_per_day[i-1]
            to_index = sum(data_points_per_day[:i+1]) - self.hold_duration
            clean_indices.append((from_index, to_index))
        
        # Clean label history
        label = pd.concat([label[from_index:to_index] for from_index, to_index in clean_indices])
        
        # Clean indicator history
        for indicator_type, indicators_history in self.indicators_history_by_indicator_type.items():
            for idx, indicator_history in enumerate(indicators_history):
                clean_indicator = np.concatenate([indicator_history[from_index:to_index] for from_index, to_index in clean_indices])
                self.indicators_history_by_indicator_type[indicator_type][idx] = clean_indicator
        
        
        ##################
        ## Format data for training
        ##################
        data = np.empty(shape=(len(label), 0))
        feature_name = []
        for indicator_type, indicators_history in self.indicators_history_by_indicator_type.items():
            for k_step, indicator_history in enumerate(indicators_history):
                data = np.append(data, indicator_history.reshape(len(indicator_history), 1), axis=1)
                feature_name.append(f"{indicator_type}-{k_step}")
        data_set = lgb.Dataset(data=data, label=label, feature_name=feature_name, free_raw_data=False).construct()
        
        
        ######################
        ## Training
        ######################
        params = {'max_depth' : self.max_depth, 'num_leaves': self.num_leaves, 'seed' : 1234}
        self.model = lgb.train(params, train_set = data_set, num_boost_round = self.num_trees, feature_name = feature_name)
        
        
    def predict_direction(self):
        """
        Predicts the direction of future returns
        """
        if self.model is None or not self.allow_predictions:
            return 0
        
        input_data = [[]]
        for _, indicators in self.indicators_by_indicator_type.items():
            for indicator in indicators:
                input_data[0].append(indicator.Current.Value)
                
        return_prediction = self.model.predict(input_data)
        if return_prediction > self.cost:
            return 1
        if return_prediction < -self.cost:
            return -1
        return 0
        
        
    def dispose(self):
        """
        Removes the indicator consolidators
        
        Input:
         - remove_events
            Flag to remove scheduled events
        """
        for consolidator in self.indicator_consolidators:
            self.SubscriptionManager.RemoveConsolidator(self.symbol, consolidator)
        
        for event in self.events:
            self.algorithm.Schedule.Remove(event)
        
            
    def start_predicting(self):
        """
        Enable the gradient boosting model to generate predictions
        """
        self.allow_predictions = True
        
        
    def stop_predicting(self):
        """
        Disable the gradient boosting model from generating predictions
        """
        self.allow_predictions = False