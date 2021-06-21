class BuyAndHold(QCAlgorithm):

    def Initialize(self):
        
        self.SetStartDate(2013, 1, 1)  #Set Start Date
        self.SetEndDate(2021, 6, 1)    #Set End Date
        self.SetCash(10000)           #Set Strategy Cash
        self.SetBrokerageModel(BrokerageName.GDAX,AccountType.Cash)
        
        self.AddCrypto("BTCUSD", Resolution.Hour)

    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.

        Arguments:
            data: Slice object keyed by symbol containing the stock data
        '''
        if not self.Portfolio.Invested:
            self.SetHoldings("BTCUSD", 1)