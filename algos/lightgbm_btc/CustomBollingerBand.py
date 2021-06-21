class CustomBollingerBand(PythonIndicator):
    """
    An extension of the BollingerBands indicator where the indicator value is
    (close - middle_band) / (2 * std)
    """
    def __init__(self, period, k):
        """
        Input:
         - period
            Period of BollingerBands indicator
         - k
            k of BollingerBands indicator
        """
        self.bb = BollingerBands(period, k)
        self.Time = datetime.min
        self.Value = 0
        self.WarmUpPeriod = self.bb.WarmUpPeriod


    def Update(self, *args):
        """
        Called each time an indicator should be updated with new data
        
        Input:
         - *args
            (1) IndicatorDataPoint
            (2) Timestamp, Float
        """
        if len(args) == 1: # Called with IndicatorDataPoint
            input = args[0]
            self.bb.Update(input.Time, input.Close)
            self.Time = input.EndTime
            self.set_value()
            return self.bb.IsReady
        else:              # Called with time and close arguments
            time, close = args[0], args[1]
            self.bb.Update(time, close)
            self.set_value()
        
    @property
    def IsReady(self):
        """
        Signals if the indicator is ready
        """
        return self.bb.IsReady
    
    def set_value(self):
        """
        Sets the current value of the indicator
        """
        std = self.bb.StandardDeviation.Current.Value
        if std == 0:
            self.Value = 0
        else:
            close = self.bb.Current.Value
            middle_band = self.bb.MiddleBand.Current.Value
            self.Value = (close - middle_band) / (2 * std)