
# Idea: An NVT Signal indicator that can also tell you when NVT crosses or
# deviates significantly from the NVTS (smoothed indicator).

# What is NVT (Network Value to Transaction)?
#   Median(14) of [Bitcoin market cap / Daily transaction volume in USD]
# What is NVTS?
#   Bitcoin market cap / 90MA of Daily transaction volume in USD
# Note: the 14-day median is applied to negate the sawtooth pattern on transaction volume.
# Intention: To detect when Bitcoin is overvalued/undervalued compared to the
# utility it serves beyond what numbers in a database (on exchange) can.
# "How much is Bitcoin worth compared to the value moved on its blockchain?"

# Credits to Willy Woo & Chris Burniske (NVT Ratio), Dimitry Kalichkin (NVT Signal)

# Goal: Show NVTS, NVT Ratio, an MA representing the long-term trend,
# highlight significant deviation from that trend, highlight "oversold" and
# "overbought" backgrounds based on absolute value of NVTS.
# Feel free to apply other indicators on NVTS, such as Bollinger Bands.

import statistics as stat

class NVTS(QCAlgorithm):

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''
        
        # QUANDL:BCHAIN/ETRVU is USD-denominated daily transaction value on BTC blockchain
        # QUANDL:BCHAIN/MKTCP is USD-denominated Bitcoin marketcap
        self.etrvu = "BCHAIN/ETRVU"
        self.mktcp = "BCHAIN/MKTCP"
        
        # ## Optional argument - personal token necessary for restricted dataset
        # Quandl.SetAuthCode("")
        
        self.SetStartDate(2014,1,1)                                 #Set Start Date
        self.SetEndDate(datetime.today())                           #Set End Date
        self.SetCash(25000)                                         #Set Strategy Cash
        
        self.AddData(QuandlCustomColumns, self.etrvu, Resolution.Daily, TimeZones.NewYork)
        self.AddData(QuandlCustomColumns, self.mktcp, Resolution.Daily, TimeZones.NewYork)
        
        self.SetBrokerageModel(BrokerageName.Bitfinex, AccountType.Cash)
        symbol = self.AddCrypto("BTCUSD", Resolution.Daily).Symbol
        
        
        
        self.med_nvt = 14                       # Median period in NVT Ratio
        self.ma_nvts = 90                       # MA used in NVTS
        self.nvts_ma_periods = 90               # MA used in RMA of NVTS (deviation base)
        self.nvts_deviation_threshold = 0.35    # Deviation threshold from RMA
        self.overbought_threshold = 150         # 'Overbought' NVTS value
        self.oversold_threshold = 60            # 'Oversold' NVTS value"
        
        # 90 day MA of Tx volume
        self.etrvu_ma = self.SMA(self.etrvu, self.ma_nvts, Resolution.Daily) 
        
        # 14 day NVT (before taking median)
        self.nvt_not_medianed = RollingWindow[float](self.med_nvt + 1)
        
        # 90 day history of NVTS
        self.nvtsHistory = RollingWindow[float](self.nvts_ma_periods + 1)
        
        
        
        self.previous = None
        
        self.SetBenchmark("BTCUSD")
        
        # Chart - Master Container for the Stock Chart:
        stockPlot = Chart("Trade Plot")
        # On the Trade Plotter Chart we want 3 series: trades and price:
        stockPlot.AddSeries(Series("Buy", SeriesType.Scatter, 0))
        stockPlot.AddSeries(Series("Sell", SeriesType.Scatter, 0))
        stockPlot.AddSeries(Series("Price", SeriesType.Line, 0))
        self.AddChart(stockPlot)
        
        
        NVTSPlot = Chart("NVTS Plot")
        NVTSPlot.AddSeries(Series("NVT Signal Significant deviation", SeriesType.Scatter, 0))
        NVTSPlot.AddSeries(Series("Buy", SeriesType.Scatter, 0))
        NVTSPlot.AddSeries(Series("Sell", SeriesType.Scatter, 0))
        NVTSPlot.AddSeries(Series( "NVT Signal 90day MA", SeriesType.Line, 0))
        NVTSPlot.AddSeries(Series("NVT Signal", SeriesType.Line, 0))
        self.AddChart(NVTSPlot)



    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
        Arguments:
            data: Slice object keyed by symbol containing the stock data
        '''
        
        mktcap = self.Securities[self.mktcp].Price
        txValue = self.Securities[self.etrvu].Price
        
        # NVT = market cap / tx Value
        self.nvt_not_medianed.Add(mktcap / txValue)
        
        if not (self.nvt_not_medianed.IsReady):
            return
        
        # NVT ratio = 14 day median of NVT
        nvtratio = stat.median(self.nvt_not_medianed)
        
        self.Plot("NVT ratio", "14 day Median", nvtratio)
        
        #-----------------------------------------------------------
        
        if not (self.etrvu_ma.IsReady):
            return
        
        etrvu_ma = self.etrvu_ma.Current.Value
        # self.Plot("NVT ratio", "estimated Tx volume", self.etrvu_ma90.Current.Value)
        
        nvts = mktcap / etrvu_ma
        self.nvtsHistory.Add(nvts)
        self.Plot("NVTS Plot", "NVT Signal", nvts)
        
        if not (self.nvtsHistory.IsReady):
            return
        
        # Create 90 day WWMA for nvts rollingWindow
        # Casting the RollingWindow to a list then a df to use .ewn().mean()
        # .iloc[-1,0] to get the most recent value of nvts_ma
        nvts_ma = pd.DataFrame(list(self.nvtsHistory)).ewm(span=self.nvts_ma_periods,adjust=False).mean().iloc[-1,0]
        self.Plot("NVTS Plot", "NVT Signal 90day MA", nvts_ma)
       
        # Mean absolute deviation
        nvts_ma_deviation = abs((nvts-nvts_ma)/nvts_ma)
        
        # Create boolean condition representing deviation
        c_deviation = nvts_ma_deviation > self.nvts_deviation_threshold
        # Create boolean condition for absolute overbought/oversold
        c_overbought = nvts > self.overbought_threshold
        c_oversold = nvts < self.oversold_threshold
        
        
        # Plotting trading signals
        if c_deviation:
            self.Plot("NVTS Plot", "NVT Signal Significant deviation", nvts)
        if c_deviation and c_oversold:
                self.Plot("NVTS Plot", "Buy", nvts)
        if c_deviation and c_overbought:
                self.Plot("NVTS Plot", "Sell", nvts)
        
        # only once per day
        if self.previous is not None and self.previous.date() == self.Time.date():
            return
        
        if not self.Portfolio.Invested:
            if c_deviation and c_oversold:
                self.Plot("Trade Plot", "Buy", self.Securities["BTCUSD"].Close)
                self.Log("BUY  >> " + str(self.Securities["BTCUSD"].Price))
                self.SetHoldings("BTCUSD", 1.0)
            return
        else:
            if c_deviation and c_overbought:
                self.Plot("Trade Plot", "Sell", self.Securities["BTCUSD"].Close)
                self.Log("SELL >> " + str(self.Securities["BTCUSD"].Price))
                self.Liquidate("BTCUSD")

        self.previous = self.Time

    def OnOrderEvent(self, orderEvent):
        self.Debug("{} {}".format(self.Time, orderEvent.ToString()))

    def OnEndOfAlgorithm(self):
        self.Log("{} - TotalPortfolioValue: {}".format(self.Time, self.Portfolio.TotalPortfolioValue))
        self.Log("{} - CashBook: {}".format(self.Time, self.Portfolio.CashBook))
        
    def OnEndOfDay(self, symbol):
       #Log the end of day prices:
       self.Plot("Trade Plot", "Price", self.Securities["BTCUSD"].Close)
       
        
# Quandl often doesn't use close columns so need to tell LEAN which is the "value" column.
class QuandlCustomColumns(PythonQuandl):
    '''Custom quandl data type for setting customized value column name. Value column is used for the primary trading calculations and charting.'''
    def __init__(self):
        # Define ValueColumnName: cannot be None, Empty or non-existant column name
        self.ValueColumnName = "Value"
