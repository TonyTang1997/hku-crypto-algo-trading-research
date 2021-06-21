# https://www.quantconnect.com/forum/discussion/6695/competition-algorithm-example-tiingo-nlp-sentiment

from QuantConnect.Data.Custom.Tiingo import *
from datetime import datetime, timedelta
import numpy as np

class CompetitionExampleAlgorithm(QCAlgorithm):

    def Initialize(self):
        
        self.SetStartDate(2014, 10, 1) 
        self.SetCash(100000)
        
        ## Set Universe Selection Model
        self.SetUniverseSelection(TechnologyETFUniverse())
        
        ## Set Alpha Model
        self.SetAlpha(NewsSentimentAlphaModel())

        ## Set Portfolio Construction Model
        self.SetPortfolioConstruction(InsightWeightingPortfolioConstructionModel())

        ## Set Execution Model
        self.SetExecution(ImmediateExecutionModel())

        ## Set Risk Management Model
        self.SetRiskManagement(NullRiskManagementModel())
        
        
class NewsSentimentAlphaModel:
    
    def __init__(self):
        
        # the sample pool of word sentiments
        self.wordSentiment = {
            "bad": -0.5, "good": 0.5, "negative": -0.5, 
            "great": 0.5, "growth": 0.5, "fail": -0.5, 
            "failed": -0.5, "success": 0.5, "nailed": 0.5,
            "beat": 0.5, "missed": -0.5, "profitable": 0.5,
            "beneficial": 0.5, "right": 0.5, "positive": 0.5, 
            "large":0.5, "attractive": 0.5, "sound": 0.5, 
            "excellent": 0.5, "wrong": -0.5, "unproductive": -0.5, 
            "lose": -0.5, "missing": -0.5, "mishandled": -0.5, 
            "un_lucrative": -0.5, "up": 0.5, "down": -0.5,
            "unproductive": -0.5, "poor": -0.5, "wrong": -0.5,
            "worthwhile": 0.5, "lucrative": 0.5, "solid": 0.5
        }
        self.day = -1
        self.custom = []
        
    
    def Update(self, algorithm, data):
        insights = []
        
        # Run the model daily
        if algorithm.Time.day == self.day:
            return insights
            
        self.day = algorithm.Time.day
        
        
        weights = {}
        
        # Fetch the wordSentiment data for the active securities and trade on any
        for security in self.custom:
            
            if not data.ContainsKey(security):
                continue
                
            news = data[security]
            
            descriptionWords = news.Description.lower().split(" ")
            # Get the intersection words between sentiment sample pool and news description
            intersection = set(self.wordSentiment.keys()).intersection(descriptionWords)
            # Calculate the score sum of word sentiment
            sentimentSum = sum([self.wordSentiment[i] for i in intersection])

            if sentimentSum > 0:
                weights[security.Underlying] = sentimentSum
        
        # Sort securities by sentiment ranking, 
        count = min(10, len(weights)) 
        if count == 0:
            return insights
            
        # Order the sentiment by value and select the top 10
        sortedbyValue = sorted(weights.items(), key = lambda x:x[1], reverse=True)
        selected = {kv[0]:kv[1] for kv in sortedbyValue[:count]}
        
        # Populate the list of insights with the selected data where the sentiment sign is the direction and its value is the weight
        closeTimeLocal = Expiry.EndOfDay(algorithm.Time)
        for symbol, weight in selected.items():
            insights.append(Insight.Price(symbol, closeTimeLocal, InsightDirection.Up, None, None, None, abs(weight)))
            
        return insights
        
        
    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            # Tiingo's News is for US Equities
            if security.Type == SecurityType.Equity:
                self.custom.append(algorithm.AddData(TiingoNews, security.Symbol).Symbol)