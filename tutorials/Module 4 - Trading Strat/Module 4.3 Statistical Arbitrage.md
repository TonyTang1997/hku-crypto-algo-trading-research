### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br>

# <ins> 4.3 Statistical Arbitrage <ins/>

## Pre-requisites

- [Module 2.2 Introduction to Machine Learning](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%202%20-%20Data%20Science%20and%20Machine%20Learning/Module%202.2%20Introduction%20to%20Machine%20Learning.md)
- [Module 3.1 Basics maths of quantitative finance](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/tutorials/Module%203%20-%20Quantitative%20Finance)
- [Module 3.3 Working with Quantconnect platform](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/tutorials/Module%203%20-%20Quantitative%20Finance)
- [Module 4.1 Moving Average Trend Following](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%204%20-%20Trading%20Strat/Module%204.1%20Moving%20Average%20Trend%20Following.md)
- [Module 4.2 Bollinger Band Mean Reverting](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%204%20-%20Trading%20Strat/Module%204.2%20Bollinger%20Band%20Mean%20Reverting.md)


## Estimated Time to Finish:
3.5 - 4 hour

## Main Learning Objectives:
- Understanding the concept stationary and mean reversion time series
- How to apply statistical to find out good pairs for trading
- Implementing statistical arbitrage strategy in quantconnect

---
## Statistical arbitrage

[Basic Statistical Arbitrage: Understanding the Math Behind Pairs Trading -- Quantopian](<https://www.youtube.com/watch?v=g-qvFjvyqcs>)

Statistical arbitrage (or stat arb) refers to a group of trading strategies that utilize mean reversion analyses to invest in diverse portfolios of up to thousands of securities for a very short period of time, often only a few seconds but up to multiple days.

Statistical arbitrage strategies are market neutral because they involve opening both a long position and short position simultaneously to take advantage of inefficient
pricing in correlated securities. For example, if a fund manager believes Coca-Cola is undervalued and Pepsi is overvalued, they would open a long position in
Coca-Cola, and at the same time, open a short position in Pepsi. Investors often refer to statistical arbitrage as “pairs trading.”

## Stationary Time Series

A collection of random variables is defined to be a stochastic or random process. A stochastic process is said to be stationary if its mean and variance are time
invariant (constant over time). A stationary time series will be mean reverting in nature, i.e. it will tend to return to its mean and fluctuations around the mean will
have roughly equal amplitudes. A stationary time series will not drift too far away from its mean because of its finite constant variance. A non-stationary time series,
on the contrary, will have a time varying variance or a time varying mean or both, and will not tend to revert back to its mean. In the financial industry, traders take
advantage of stationary time series by placing orders when the price of a security deviates considerably from its historical mean, speculating the price to revert back
to its mean. They start by testing for stationarity in a time series.

## Cointegration Tests

Cointegration tests identify scenarios where two or more non-stationary time series are integrated together in a way that they cannot deviate from equilibrium in the
long term. The tests are used to identify the degree of sensitivity of two variables to the same average price over a specified period of time. The Johansen test is
used to test cointegrating relationships between several non-stationary time series data. Compared to the Engle-Granger test, the Johansen test allows for more than one
cointegrating relationship. However, it is subject to asymptotic properties (large sample size) since a small sample size would produce unreliable results. Using the
test to find cointegration of several time series avoids the issues created when errors are carried forward to the next step.

# <ins> Trading Logic <ins/>

We have an example here implementing a statistical arbitrage strategy with the pair of BTC and ETH.

1. Calculating the spread and hedge weights with a linear regression

2. When the spread moves away from the moving average more than a certain amount of the moving standard deviation, (long BTC - short ETH) or (short ETH - long BTC) accordingly.

3. When the spread comes back to the moving average, close all the positions.

#### Link to code
[link to code](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/algos/btc_eth_stat_arb.py)

---
## Next up:

[Module 4.4 Gradient Boosting Decision Trees based Model](<./Module 4.4 Gradient Boosting Decision Trees based Model.md>)

---

## References
  - [Statistical Arbitrage - Investopedia](https://www.investopedia.com/terms/s/statisticalarbitrage.asp)

  - [Basic Statistical Arbitrage: Understanding the Math Behind Pairs Trading -- Quantopian](<https://www.youtube.com/watch?v=g-qvFjvyqcs>)
