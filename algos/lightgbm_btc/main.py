# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *

from GradientBoostingAlphaModel import GradientBoostingAlphaModel

class GradientBoostingModelAlgorithm(QCAlgorithm):

    def Initialize(self):
        
        self.SetStartDate(2015, 9, 1)
        self.SetEndDate(2020, 9, 17)
        
        self.SetCash(1000000)
        
        symbols = [ Symbol.Create("BTCUSD", SecurityType.Crypto, Market.Bitfinex) ]
        self.SetUniverseSelection( ManualUniverseSelectionModel(symbols) )
        self.UniverseSettings.Resolution = Resolution.Hour
        
        self.SetAlpha(GradientBoostingAlphaModel())
        
        self.SetPortfolioConstruction(InsightWeightingPortfolioConstructionModel())
        
        self.SetExecution(ImmediateExecutionModel())