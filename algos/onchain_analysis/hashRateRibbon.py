# Credits to Charles Edwards

# IDEA: When miners give up, it is possibly the most powerful Bitcoin buy signal ever.
# Buying during Miner Capitulation yields wonderful returns.
# The best buy signals occur on Hash Rate "recovery", and when price momentum is also positive.

# A simple 1- and 2-month simple moving average of Bitcoin’s Hash Rate
# can be used to identify market bottoms, miner capitulation
# and — even better — great times to buy Bitcoin.

# Source:
# Hash Ribbons & Bitcoin Bottoms by Charles Edwards
# https://medium.com/capriole/hash-ribbons-bitcoin-bottoms-60da13095836
# Takeaways:
    # Hash Rate leads Difficulty in identifying Bitcoin Miner Capitulation
    # Buying during Miner Capitulation, when the Hash Rate starts to recover, is a wonderful strategy
    # Going one step further, the majority of all draw downs can be eliminated from this strategy 
    #   by waiting until the 10-day price SMA is above the 20 day price SMA
    # Next time you see the Hash Ribbon buy signal, you would be wise to pay attention
        

class HashrateRibbon(QCAlgorithm):

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''

        self.hashrate = "BCHAIN/HRATE"
        self.SetStartDate(2013,1,1)                                 #Set Start Date
        self.SetEndDate(datetime.today())                           #Set End Date
        self.SetCash(25000)                                         #Set Strategy Cash
        self.AddData(QuandlCustomColumns, self.hashrate, Resolution.Daily, TimeZones.NewYork)
        
        
        self.SetBrokerageModel(BrokerageName.Bitfinex, AccountType.Cash)
        symbol = self.AddCrypto("BTCUSD", Resolution.Daily).Symbol
        
        # Hash rate ribbon
        
        self.hrPeriodFast = 30
        self.hrPeriodSlow = 60
        
        self.hrFast = self.SMA(self.hashrate, self.hrPeriodFast, Resolution.Daily)
        self.hrSlow = self.SMA(self.hashrate, self.hrPeriodSlow, Resolution.Daily)
        
        self.hrFastHisotry = RollingWindow[float](self.hrPeriodFast + 1)
        self.hrSlowHistory = RollingWindow[float](self.hrPeriodSlow + 1)
        
        self.hrCrossAbove = False
        self.hrCrossBelow = False
        
        # SMA cross
        
        self.periodFast = 10
        self.periodSlow = 20
        
        self.fast = self.SMA(symbol, self.periodFast, Resolution.Daily)
        self.slow = self.SMA(symbol, self.periodSlow, Resolution.Daily)
        
        self.FastHisotry = RollingWindow[float](self.periodFast + 1)
        self.SlowHistory = RollingWindow[float](self.periodSlow + 1)
        
        self.previous = None
        
        self.SetBenchmark("BTCUSD")
        
        # Chart - Master Container for the Chart:
        stockPlot = Chart("Trade Plot")
        # On the Trade Plotter Chart we want 3 series: trades and price:
        stockPlot.AddSeries(Series("Buy", SeriesType.Scatter, 0))
        stockPlot.AddSeries(Series("Sell", SeriesType.Scatter, 0))
        stockPlot.AddSeries(Series("Price", SeriesType.Line, 0))
        self.AddChart(stockPlot)



    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
        Arguments:
            data: Slice object keyed by symbol containing the stock data
        '''
        self.FastHisotry.Add(self.fast.Current.Value)
        self.SlowHistory.Add(self.slow.Current.Value)
        self.hrFastHisotry.Add(self.hrFast.Current.Value)
        self.hrSlowHistory.Add(self.hrSlow.Current.Value)
        
        if not (self.slow.IsReady and self.hrSlow.IsReady):
            return
        
        self.Plot("HR", "HR Oscillator", self.Oscillator(self.hrFastHisotry,self.hrSlowHistory))
        
        # only once per day
        if self.previous is not None and self.previous.date() == self.Time.date():
            return
        
        # define a small tolerance on our checks to avoid bouncing
        tolerance = 0.00015
        
        
        # Creating a flag to check for hash rate crosses.
        # If True, the flags remain true until the an order has been placed, or
        # when the opposite flag is true
        if not self.hrCrossAbove:
            self.hrCrossAbove = self.CrossAbove(self.hrFastHisotry,self.hrSlowHistory)
            if self.hrCrossAbove: self.hrCrossBelow = False 
            
        if not self.hrCrossBelow:
            self.hrCrossBelow = self.CrossBelow(self.hrFastHisotry,self.hrSlowHistory)
            if self.hrCrossBelow: self.hrCrossAbove = False 
            
        # Buy when crossabove has already occured and fast price SMA is under the slower one too    
        if not self.Portfolio.Invested:
            if (self.fast.Current.Value > self.slow.Current.Value * (1 + tolerance)) and self.hrCrossAbove:
                self.Log("BUY  >> " + str(self.Securities["BTCUSD"].Price))
                self.SetHoldings("BTCUSD", 1.0)
                self.Plot("Trade Plot", "Buy", self.Securities["BTCUSD"].Price)
                self.hrCrossAbove = False
                
            return
        else:
        # Sell when crossbelow has already occured and fast price SMA is under the slower one too 
            if self.hrCrossBelow and (self.fast.Current.Value < self.slow.Current.Value * (1 + tolerance)):
                self.Log("SELL >> " + str(self.Securities["BTCUSD"].Price))
                self.Liquidate("BTCUSD")
                self.Plot("Trade Plot", "Sell", self.Securities["BTCUSD"].Price)
                self.hrCrossBelow = False

        self.previous = self.Time
        
        # self.Plot("Benchmark", "hrFast", self.hrFast.Current.Value)
        # self.Plot("Benchmark", "hrSlow", self.hrSlow.Current.Value)
        # self.Plot("Benchmark", "fast", self.fast.Current.Value)
        # self.Plot("Benchmark", "slow", self.slow.Current.Value)
        # self.Plot("Benchmark", "BTCUSD", self.Securities["BTCUSD"].Price)

    def OnOrderEvent(self, orderEvent):
        self.Debug("{} {}".format(self.Time, orderEvent.ToString()))

    def OnEndOfAlgorithm(self):
        self.Log("{} - TotalPortfolioValue: {}".format(self.Time, self.Portfolio.TotalPortfolioValue))
        self.Log("{} - CashBook: {}".format(self.Time, self.Portfolio.CashBook))
        
    def OnEndOfDay(self, symbol):
       #Log the end of day prices:
       self.Plot("Trade Plot", "Price", self.Securities["BTCUSD"].Close)
       
    # Check if window 1 crosses above window 2   
    def CrossAbove(self, window1, window2, tolerance=0):
        
        return window1[0] > window2[0] * (1 + tolerance) and window1[1] < window2[1] * (1 - tolerance)
        
    # Check if window 1 crosses below window 2  
    def CrossBelow(self, window1, window2, tolerance = 0):
        
        return window1[0] < window2[0] * (1 - tolerance) and window1[1] > window2[1] * (1 + tolerance)
    
    # An oscillator based on percentage differences
    def Oscillator(self, window1, window2):
        return (window1[0] - window2[0])/window1[0] * 100
        
# Quandl often doesn't use close columns so need to tell LEAN which is the "value" column.
class QuandlCustomColumns(PythonQuandl):
    '''Custom quandl data type for setting customized value column name. Value column is used for the primary trading calculations and charting.'''
    def __init__(self):
        # Define ValueColumnName: cannot be None, Empty or non-existant column name
        self.ValueColumnName = "Value"
