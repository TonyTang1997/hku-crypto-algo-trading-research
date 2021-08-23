### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br

## Pre-requisites
- [Module 2.1 Pandas](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%202%20-%20Data%20Science%20and%20Machine%20Learning/Module%202.1%20Pandas.md)
- [Module 2.2 Introduction to Machine Learning](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%202%20-%20Data%20Science%20and%20Machine%20Learning/Module%202.2%20Introduction%20to%20Machine%20Learning.md)
- [Module 3.3 Working with Quantconnect platform](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/tutorials/Module%203%20-%20Quantitative%20Finance)
- [Module 4.2 Bollinger Band Mean Reverting](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/blob/main/tutorials/Module%204%20-%20Trading%20Strat/Module%204.2%20Bollinger%20Band%20Mean%20Reverting.md)

## Estimated Time to Finish:
1.5 - 2 hour

## Main Learning Objectives:
- Understanding the basic of Gradient Boosting Decision Trees
- Implementing Gradient Boosting Decision Trees strategy in quantconnect


# <ins> 4.4 Gradient Boosting Decision Trees <ins/>

A decision tree is a machine learning model that builds upon iteratively asking questions to partition data and reach a solution. It is the most intuitive way to zero
in on a classification or label for an object. Visually too, it resembles and upside down tree with protruding branches and hence the name.

A decision tree is a flowchart-like tree structure where each node is used to denote feature of the dataset, each branch is used to denote a decision, and each leaf
node is used to denote the outcome.

Ensemble learning, in general, is a model that makes predictions based on a number of different models. By a combining a number of different models, an ensemble learning tends to be more flexible (less bias) and less data sensitive (less variance).

The two most popular ensemble learning methods are bagging and boosting.
1. Bagging : Training a bunch of models in parallel way. Each model learns from a random subset of the data.
  - [Bootstrap Aggregating (Bagging)](https://www.youtube.com/watch?v=2Mg8QD0F1dQ) explained

2. Boosting : Training a bunch of models sequentially. Each model learns from the mistakes of the previous model.
  - [Boosting EXPLAINED! - CodeEmporium](https://www.youtube.com/watch?v=MIPkK5ZAsms)
    - Explains the rationale behind boosting and the difference between AdaBoost and Gradient Boost
  - [Gradient Boost Part 1 (of 4): Regression Main Ideas](https://www.youtube.com/watch?v=3CC4N4z3GJc)
    - Optional video series on how Gradient Boosting works

Boosting works on the principle of improving mistakes of the previous learner through the next learner.

In boosting, weak learner are used which perform only slightly better than a random chance.
Boosting focuses on sequentially adding up these weak learners and filtering out the observations that a learner gets correct at every step. Basically the stress is on
developing new weak learners to handle the remaining difficult observations at each step.

# <ins> Trading Logic <ins/>

The strategy is bulit on Module 4.2 Bollinger Band Mean Reverting, we apply a GBDT model to decide we want to follow the suggestions from Bollinger Band or not.


#### Link to code
[link to code](https://github.com/TonyTang1997/hku-crypto-algo-trading-research/tree/main/algos/lightgbm_btc)


---
## Next up:

[Module 4.5 Deep Learning based Model](<./Module 4.5 Deep Learning based Model.md>)

---

## References
  - [Bootstrap AGgregating (Bagging)](https://www.youtube.com/watch?v=2Mg8QD0F1dQ)
  - [Boosting EXPLAINED! - CodeEmporium](https://www.youtube.com/watch?v=MIPkK5ZAsms)
  - [Gradient Boost Part 1 (of 4): Regression Main Ideas](https://www.youtube.com/watch?v=3CC4N4z3GJc)
