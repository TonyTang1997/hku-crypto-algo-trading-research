### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br>

# <ins> 4.2 Bollinger Band Mean Reverting <ins/>

## Pre-requisites
- [Module 2.1 Pandas](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%202%20-%20Data%20Science%20and%20Machine%20Learning/Module%202.1%20Pandas.md)
- [Module 3.1 Basic math of quantitative finance](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/tutorials/Module%203%20-%20Quantitative%20Finance)
- [Module 3.3 Working with Quantconnect platform](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/tutorials/Module%203%20-%20Quantitative%20Finance)
- [Module 4.1 Moving Average Trend Following](<./Module 4.1 Moving Average Trend Following.md>)

## Estimated Time to Finish:
1.5 - 2 hour

## Main Learning Objectives:
- Understanding the definitions of bollinger band
- How to apply bollinger band as trading signals
- Implementing bollinger band mean reverting strategy in quantconnect


## Bollinger Bands

[How to Use Bollinger Bands - TD Ameritrade](https://www.youtube.com/watch?v=AWN-jpnRwJg)

Bollinger Band utilises basic statistical concepts, including mean and standard deviation, to identify the price range of assets.   

Bollinger Band is built on a simple moving average. We first calculate a SMA of a certain time horizon, then the upper band is derived by adding the rolling standard deviation of the prices during the same time horizon and the lower band is derived by subtracting the rolling standard deviation of the prices during the same time horizon.


## <ins> Usages of the indicators <ins/>

Here are some of the common applications of the Bollinger Band.

1. When the band gets narrower due to a period of lower volatility, there is higher possibility for the price to move sharply on either direction, leading to a higher volatility period.

2. For some assets, the prices have a high tendency to bounce within the upper and lower bands, touching one band then revert to the moving average. We can trade a mean reverting strategy if we identify these trends.

3. The breakout of the price to either one of the upper or lower bands is a major event and indicating the instrument has enter another regime.

## <ins> Trading Logic <ins/>

When the price of the instrument touches either band, we expect that it will revert back to it's moving average.

- When the price is larger than the upper band, take a short position

- When the price is lower than the lower band, take a long position.

- When we have a short position and the price is lower than the moving average, liquidate all the positions.

- When we have a long position and the price is larger than the moving average, liquidate all the positions.

#### Link to code
[link to code](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/algos/bband.py)

---
## Next up:

[Module 4.3 Statistical Arbitrage](<./Module 4.3 Statistical Arbitrage.md>)

---

## References
  - [How to Use Bollinger Bands - TD Ameritrade](https://www.youtube.com/watch?v=AWN-jpnRwJg)
