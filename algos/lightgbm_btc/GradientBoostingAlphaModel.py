from SymbolData import SymbolData


class GradientBoostingAlphaModel(AlphaModel):
    """
    Emits insights in the direction of the prediction made by the Symbol Data objects.
    """
    symbol_data_by_symbol = {}
    
    def __init__(self, hold_duration = 10):
        """
        Input:
         - hold_duration
            The duration of the insights emitted
        """
        self.hold_duration = hold_duration 
        self.weight = 1
    
    
    def Update(self, algorithm, data):
        """
        Called each time the alpha model receives a new data slice.
        
        Input:
         - algorithm
            Algorithm instance running the backtest
         - data
            A data structure for all of an algorithm's data at a single time step
        
        Returns a list of Insights to the portfolio construction model.
        """
        insights = []
        for symbol, symbol_data in self.symbol_data_by_symbol.items():
            direction = symbol_data.predict_direction()
            if direction:
                hold_duration = timedelta(minutes=self.hold_duration) # Should match universe resolution
                insights.append(Insight.Price(symbol, hold_duration, direction, None, None, None, self.weight))

        return insights
        
        
    def OnSecuritiesChanged(self, algorithm, changes):
        """
        Called each time the universe has changed.
        
        Input:
         - algorithm
            Algorithm instance running the backtest
         - changes
            The additions and removals of the algorithm's security subscriptions
        """
        for security in changes.AddedSecurities:
            symbol = security.Symbol
            self.symbol_data_by_symbol[symbol] = SymbolData(symbol, algorithm, self.hold_duration)
            
        for security in changes.RemovedSecurities:
            symbol_data = self.symbol_data_by_symbol.pop(security.Symbol, None)
            if symbol_data:
                symbol_data.dispose()
        
        self.weight = 1 / len(self.symbol_data_by_symbol)