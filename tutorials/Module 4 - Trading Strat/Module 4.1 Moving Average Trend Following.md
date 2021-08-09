### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br>

# <ins> Moving Average Trend Following <ins/>

Moving Average is a family of most well-known technical indicators adopted by different traders.

The formal statistical definition of moving average is the calculation of averages of different subsets (rolling window) of all the observations.

The main motivation of using a moving average is to reduce noise from our observations so that we can spot the trend from a security's price data more easily.

There many different kinds of moving averages and we are going to cover three of them,

1. Simple Moving Average

2. Volume Weighted Moving Average

3. Exponential Weighted Moving Average

## Simple Moving Average

Simple Moving Average (SMA) is the most basic form of a moving average which is taking the arithmetic mean of a rolling window of data.

Definition of arithmetic mean : the sum of a collection of numbers divided by the count of numbers in the collection.

Simple Moving Average is easy to be implemented and understood by traders and effective to smooth a raw price time series. However, it gives the same weightings to trade observations with different volume or occurred at different time.

Volume Weighted Moving Average and Exponentially Weighted Moving Average are enchancement of SMA.

## Volume Weighted Moving Average

Volume Weighted Moving Average (VWMA) highlights the importance of different sizes by weighing based on the volume of each trade. Prices with more trading volume get greater weight than prices with fewer trading volume.

VWMA is calculated by summing up the dollars traded (prices multiplied by the volume of shares traded) and then dividing by the total volume of shares traded in a rolling window.

The rationale behind is that orders with large sizes are executed by institutions or multiple traders with same views on the market so that these trades would move the market more. When the sizes of orders are the same or similar, the values of SMA and VWMA are close to each other.


## Exponentially Weighted Moving Average

Exponential Weighted Moving Average (EMA) places larger weights on recent observations. EWMA responds to recent price changes more sensitively than SMA, which allocates equal weightings to all observations in the period.


# <ins> Trading Logic <ins/>

Example https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/algos/cryptos_sma_trend_following.py

We have an example here implementing a SMA cross-over strategy. 

When the current price is larger than the 210-days simple moving average, we buy the instrument. Otherwise, we liquidate our current position.

This is a very simple strategy and there are serveral improvements than you can add on it. 

1. Tuning the parameter of moving average (using different days of moving average)

2. Using different types of moving average (SMA, VWMA, EWMA)

3. Instead of the current price, placing trades when a shorter horizon moving average cross-over a longer horizon moving average.

4. The current implementation only generates buy signals, we can also follow the downward trend to generate short signals.






