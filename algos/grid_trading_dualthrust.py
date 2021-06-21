# https://www.quantconnect.com/tutorials/strategy-library/dual-thrust-trading-algorithm

from datetime import datetime

import numpy as np
import decimal as d
from datetime import timedelta


class DualThrustAlgorithm(QCAlgorithm):

    def Initialize(self):
        
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''
        
        self.SetStartDate(2015,1,1)
        self.SetEndDate(2020,1,1)
        self.SetCash(100000)
        equityt   = self.AddSecurity(SecurityType.Equity, "SPY", Resolution.Hour)
        equity    = self.AddCrypto("BTCUSD", Resolution.Daily)
        self.syls = equity.Symbol
        
        # schedule an event to fire every trading day for a security 
        # the time rule here tells it to fire when market open 
#        self.syl         = equity.Symbol
        self.syl         = "BTCUSD"
#        self.Schedule.On(self.DateRules.EveryDay(self.syl),self.TimeRules.AfterMarketOpen(self.syl,5),Action(self.SetSignal))
        self.Schedule.On(self.DateRules.EveryDay(self.syl), self.TimeRules.AfterMarketOpen(self.syl,0), Action(self.SetSignal))
        self.selltrig    = None
        self.buytrig     = None
        self.currentopen = None
    
    def SetSignal(self):
        
        """
        history = self.History(["BTCUSD",], 4, Resolution.Daily)
        self.Log(str(history))
                             close    high     low    open       volume
        symbol time                                                   
        BTCUSD 2016-12-29  982.17  983.46  923.95  926.03  9792.346831
               2016-12-30  970.72  988.88  950.50  982.28  8997.859016
               2016-12-31  960.81  970.51  930.30  970.51  7945.763020
               2017-01-01  973.26  973.37  949.00  961.52  3837.287886
        """
        history = self.History(["BTCUSD",], 4, Resolution.Daily).loc["BTCUSD"]
        
        k1         = 0.5
        k2         = 0.5
        self.high  = history.high.values.astype(np.float32)
        self.low   = history.low.values.astype(np.float32)
        self.close = history.close.values.astype(np.float32)
        
        self.Log("ss-2")
        # Pull the open price on each trading day
        self.currentopen = float(self.Portfolio[self.syl].Price)
        self.Log("ss-3")
        HH, HC, LC, LL = max(self.high), max(self.close), min(self.close), min(self.low)
        if HH - LC >= HC - LL:
            signalrange = HH - LC
        else:
            signalrange = HC - LL
        
        self.selltrig = self.currentopen - k1 * signalrange
        self.buytrig  = self.currentopen + k2 * signalrange    
    
    def OnData(self,data):
        
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.'''
        self.Log("1")
        holdings = self.Portfolio[self.syl].Quantity
        self.Log(str(self.Portfolio[self.syl].Price))
        self.Log(str(self.selltrig))
        self.Log("3")
        if self.Portfolio[self.syl].Price >= self.selltrig:
            if holdings >= 0:
                self.SetHoldings(self.syl, 0.8)
            else:
                self.Liquidate(self.syl)
                self.SetHoldings(self.syl, 0.8)
                
        elif self.Portfolio[self.syl].Price < self.selltrig:
             if holdings >= 0:
                self.Liquidate(self.syl)
                self.SetHoldings(self.syl, -0.8)
             else:
                self.SetHoldings(self.syl, -0.8)
        self.Log("3")
        self.Log("open: "+ str(self.currentopen)+" buy: "+str(self.buytrig)+" sell: "+str(self.selltrig))