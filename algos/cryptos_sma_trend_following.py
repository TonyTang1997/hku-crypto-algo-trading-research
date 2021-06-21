#https://www.quantconnect.com/tutorials/strategy-library/asset-class-trend-following

import numpy as np
from datetime import datetime

class BasicTemplateAlgorithm(QCAlgorithm):

    def Initialize(self):

        self.SetStartDate(2015, 5, 1)  
        self.SetEndDate(datetime.now())    
        self.SetCash(100000)           
        self.data = {}
        period = 10*21
        self.SetWarmUp(period)
        
        self.SetBrokerageModel(BrokerageName.GDAX,AccountType.Cash)
        
        self.symbols = ["BTCUSD", "ETHUSD", "BCHUSD"]
        
        for symbol in self.symbols:
            self.AddCrypto(symbol, Resolution.Daily)
            self.data[symbol] = self.SMA(symbol, period, Resolution.Daily)

    def OnData(self, data):
        if self.IsWarmingUp: return
        isUptrend = []
        for symbol, sma in self.data.items():
            if self.Securities[symbol].Price > sma.Current.Value:
                isUptrend.append(symbol)
            else:
                self.Liquidate(symbol)
        
        for symbol in isUptrend:
            self.SetHoldings(symbol, 1/len(isUptrend))