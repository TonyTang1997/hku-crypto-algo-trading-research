#https://www.quantconnect.com/forum/discussion/5145/crypto-bollinger-band-strategy/p1

from QuantConnect.Indicators import *


class BollingerMomentum(QCAlgorithm):

    def Initialize(self):

        self.SetStartDate(2013, 1, 1)  #Set Start Date
        self.SetEndDate(2019, 6, 1)    #Set End Date
        self.SetCash(10000)           #Set Strategy Cash
        self.SetBrokerageModel(BrokerageName.GDAX, AccountType.Cash)
        self.AddCrypto("BTCUSD", Resolution.Daily)
        
        self.position = 0
        
        ## Set Boilinger Bands
        self.bband = self.BB("BTCUSD", 20, 2, MovingAverageType.Simple, Resolution.Daily)

        # Set WarmUp period
        self.SetWarmUp(20)
        

    def OnData(self, data):
        
        price = self.Securities["BTCUSD"].Close
        
        
        ## BUY if price is larger than upper band
        if not self.Portfolio['BTCUSD'].Invested and price > self.bband.UpperBand.Current.Value:
                self.SetHoldings("BTCUSD", -1)

        if not self.Portfolio['BTCUSD'].Invested and price < self.bband.LowerBand.Current.Value:
                self.SetHoldings("BTCUSD", 1)

        ## Liquidate if price is larger than middle band        
        if self.Portfolio['BTCUSD'].IsLong and price > self.bband.MiddleBand.Current.Value:
                self.Liquidate()
                
        ## Liquidate if price is less than middle band        
        if self.Portfolio['BTCUSD'].IsShort and price < self.bband.MiddleBand.Current.Value:
                self.Liquidate()