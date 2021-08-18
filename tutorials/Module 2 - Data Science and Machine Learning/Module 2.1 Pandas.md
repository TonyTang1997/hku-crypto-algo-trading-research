### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br>

# <ins> 2.1 Pandas <ins/>

## Overview
Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

---

## Pre-requisites
- Python Basics
- Object-oriented Programming

---
## Estimated Time to Finish:
7 hours

---
## Main Learning Objectives:
- Learn how to create and manipulate DataFrames
- Learn how to turn real-time data into codes

---
## Tutorials

In this section, we are going to cover the following topics about pandas. In the turotial videos we'll walk you through the Kaggle notebook and we recommend watch them before getting your hands on the exercises on Kaggle.

- 2.1.1. Creating, Reading and Writing

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/creating-reading-and-writing)
    * [link to tutorial video](https://drive.google.com/file/d/1DgCUsq_iVxM4aUQbodeN6-yVY6ealGnG/view?usp=sharing)
    * [link to exercise video](https://drive.google.com/file/d/1XdjB16L6rLoH3HTK6dCwaL_5jjohhGPL/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        | pd.DataFrame()      | ```Dict```       | [Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>)           |
        | pd.Series()   | ```List```        |[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html>)            |
        |pd.read_csv()| File Path| [Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>)|
        |wine_reviews.head()|```n=5```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html>)|

- 2.1.2. Indexing, Selecting & Assigning

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/indexing-selecting-assigning)
    * [link to tutorial video](https://drive.google.com/file/d/1GSH6qtspbM_wdKuBl6T1iMX5CaB9LXVG/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        |reviews.iloc[]|Integer Location|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html>)|
        |reviews.loc[]|Index Label|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html>)|
        |reviews.set_index()|```string```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html>)|
        |reviews.country.isin()|```List```|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html>)|

- 2.1.3. Summary Functions and Maps

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/summary-functions-and-maps)
    * [link to tutorial video](https://drive.google.com/file/d/1EJZ6q2f9qkvnjV1TraRvNdxRZmTdxyW1/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        |reviews.describe()|```None```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>)|
        |reviews.taster_name.unique()|```None```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.unique.html>)|
        |reviews.taster_name.value_counts()|```None```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html>)|
        |reviews.points.map()|```Function```|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html>)|
        |reviews.apply()|```Function```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html>)|

- 2.1.4. Grouping and Sorting

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/grouping-and-sorting)
    * [link to tutorial video](https://drive.google.com/file/d/1Ln7nUAGJkBLwPaBa0tK5QXTOBB2IHF2T/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        |reviews.groupby()|Column Name(s)|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html>)|
        |countries_reviewed.reset_index()|```None```|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html>)|
        |countries_reviewed.sort_values()|```by={Column Name(s)}```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html>)|
        |countries_reviewed.sort_index()|```None```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html>)|

- 2.1.5. Data Types and Missing Values

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/data-types-and-missing-values)
    * [link to tutorial video](https://drive.google.com/file/d/1qX3LLcNkND9g5lPIZAZqwpyW4SX41q7H/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        |reviews.points.astype()|```string```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html>)|
        |pd.isnull()|```array```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.isnull.html>)|
        |reviews.region_2.fillna()|```string/numerical```|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html>)|
        |reviews.taster_twitter_handle.replace()|```string```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html>)|

- 2.1.6. Renaming and Combining

    * [link to the Kaggle page](https://www.kaggle.com/residentmario/renaming-and-combining)
    * [link to tutorial video](https://drive.google.com/file/d/1ifNP8mXLPBrMARDhShwmyLV8UaZjARav/view?usp=sharing)
    * API Documentation:

        | Method      | Frequently Used Arguments         |Documentation URL         |
        | ----------- | ----------- |----------- |
        |reviews.rename()|```columns=Dict```|[Link](<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html>)|
        |reviews.rename_axis()|```string```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html>)|
        |pd.concat()|```List```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.concat.html>)|
        |left.join()|```DataFrame```|[Link](<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html>)|

---
## Next Up:

You will learn [Introduction to Machine Learning](<./Module 2.2 Introduction to Machine Learning.md>) in the next section and hopefully, you will be able to develop your first ML model after learning the next section.

---
## References

- [Pandas tutorials - Kaggle](https://www.kaggle.com/learn/pandas)
