### Cryptocurrency Algorithmic Trading
HKU FinTech Competition
<br><br>

# <ins> 1.1 Basic Python <ins/>

Python is a programming language named after the British comedy troupe [Monty Python](https://en.wikipedia.org/wiki/Monty_Python).
In This chapter, we will cover the key Python skills you’ll need so you can start programming.


**Note that there are quite some optional external references included in this Module, feel free to go through or skip them at your own interest.**


## Pre-requisites
None

## Estimated Time to Finish:
3-5 hours (excluding Optional Materials)

## Main Learning Objectives:
- learning the basic syntax of python, variables, functions, arithmetic
- learning about `string`, `list`, `tuple` and `dictionary`
- learning how to import external libraries

## Learning Programming
It can take months or years to become proficient in basic programming. Many times, you'll need to review lessons several times. Programming also necessitates hands-on expertise; instead of reading/watching the examples, actively follow along on your computer. Learning programming is similar to learning how to drive a car or doing physical fitness exercises. it is not possible to attain the skills solely by reading about it and/or viewing videos.

You are recommended to read this article: [How to teach yourself hard things](https://jvns.ca/blog/2018/09/01/learning-skills-you-can-practice/)

Solving practice problems is very useful to review your understanding. After familiarizing with the basics, try experimenting with your newly acquired skills. If you get stuck, you can search online/documentation/books for those specific problems (go to the [Optional Resources](<## Optional Resources>) below for more), and if that fails, you can ask us for help.

## The Tutorial

You will be learning the basics of python from the tutorials on [*Kaggle*](https://www.kaggle.com/learn/python), a popular platform for data science competitions and also a source of useful datasets. Catered towards data science (which is relevant to algotrading),

**Kaggle** will be main learning resource for this module as the tutorials are interactive and filled with examples. You will also get to try out some exercises inside **Kaggle notebooks** after learning each subtopic.
- for Kaggle notebooks, each logged out sessions resets after 15 minutes. You can create a Kaggle account (which is free) to bypass this limitation and get the benefit of progress tracking.
- However, most exercises are short, and you probably will not need more than 15 minutes to finish them, so creating an account is not a must.
- **Make sure you run the setup cell first in each exercise before doing the questions**, refer to the [overview video](https://drive.google.com/file/d/1fSZWMmj8I5qEJ2SegIIacIOHpzxbjkUr/view?usp=sharing) for more.
- **Please do not change the line with the answer-checking function call (e.g. `q0.check(color)`)**

**The following content is the summary of the Kaggle chapters. You are advised to *finish the entire kaggle tutorial first* before referring to the below summary as a refresher.**

[*Link to tutorial: Kaggle - Learning Python*](https://www.kaggle.com/learn/python)

## Overview
1.  [Syntax](#111-syntax)
2.  [Functions](#112-functions)
3.  [Booleans & Conditions](#113-booleans--conditions)
4.  [Lists](#114-lists)
5.  [Loops and List comprehension](#115-loops-and-list-comprehension)
6.  [Strings and dictionaries](#116-strings-and-dictionaries)
7.  [Working with External Libraries](#117-working-with-external-libraries)

---

## Summary
Below is the summary of the content covered in the [**Kaggle**](https://www.kaggle.com/learn/python) tutorials. Relevant Cheatsheets from [Python Crash Course 2nd Edition](https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/) is also provided (Credit goes to the author [Eric Matthes](https://ehmatthes.github.io/))

---

### 1.1.1 Syntax

[cheatsheet (syntax)](https://drive.google.com/file/d/1xDrV2ugdKPQWpEsJGhfrjD3oES2QZ0GH/view?usp=sharing)

- `print("Strings are enclosed by double or single quotation marks")`
- arithmetic

| Operator     | Name    | Description |       
|--------------|----------------|--------------------------------------------------------|
| ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
| ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
| ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
| ``-a``       | Negation       | The negative of ``a``                                  |

- declaring variables
> **Variables** are used to assign **labels** to values.

- commenting with `#`
---


### 1.1.2 Functions

[cheatsheet (functions)](https://drive.google.com/file/d/17YNfbkFalRg6BtXAX-914FmupmzwEk7P/view?usp=sharing)

> Functions are named blocks of code, designed to do one
specific job. Information passed to a function is called an
**argument**, and information received by a function is called a
**parameter**.

```python
def double(num):
    return num*2

print(double(10))
```
In the above example, `10` is the argument, `num` is the parameter

- Getting help with `help()`
- How to define functions and write docstrings
- the `return` keyword
- function arguments
- stacking functions
---


### 1.1.3 Booleans & Conditions
[cheatsheet (if, while)](https://drive.google.com/file/d/1RNnicY97CE4PW1QP2qrA67LtqY5gKXft/view?usp=sharing)
> If statements are used to test for particular conditions and respond appropriately.

- Booleans: `True` or `False`
- Comparisons

| Operation       | Description                         |     | Operation       | Description                            |
| --------------- | ----------------------------------- | --- | --------------- | -------------------------------------- |
| ``a == b``      | ``a`` equal to ``b``                |     | ``a != b``      | ``a`` not equal to ``b``               |
| ``a < b``       | ``a`` less than ``b``               |     | ``a > b``       | ``a`` greater than ``b``               |
| ``a <= b``      | ``a`` less than or equal to ``b``   |     | ``a >= b``      | ``a`` greater than or equal to ``b``   |

- `and`, `or`, `not` keywords
- `if`, `elif`, `else` conditionals

---


### 1.1.4 Lists
[cheatsheet (list)](https://drive.google.com/file/d/1N_4crYubJg7d87tn1oJs3KwGGmd0t-Oy/view?usp=sharing)

> A list stores a series of items in a particular order. You access items using an **index**, or within a **loop**.

- indexing (first element has index 0, last element has index -1)
- slicing (`list[start:end:strides]`)
- modifying lists in place
- list functions: `len()`, `sorted()`, `sum()`, `max()`
- list methods: `.append()`, `.index()`, `.pop()`
- `in` operator
- Lists `[]` vs Tuples `{}`
> Tuples are similar to lists, but the items in a tuple can't be modified.

---

### 1.1.5 Loops and List comprehension

[cheatsheet (if, while)](https://drive.google.com/file/d/1RNnicY97CE4PW1QP2qrA67LtqY5gKXft/view?usp=sharing)

- `for` loops and `range()`
> A For loop is used to repeat a specific block of code a known number of times.

- `while` loops
> A while loop repeats a block of code as long as a certain condition is true. While loops are especially useful when you
can't know ahead of time how many times a loop should run.
- shortening your code with List comprehension

---

### 1.1.6 Strings and dictionaries
#### Strings
> A string is a series of characters, surrounded by single or double quotes.

- String syntax, manipulation

| What you type | What you get | example | `print(example)`  |
|--------------|----------------|----------------------------|----------------------------|
| `\'`         | `'`            | `'What\'s up?'`            | `What's up?`            |  
| `\"`         | `"`            | `"That's \"cool\""`        | `That's "cool"`         |  
| `\\`         | `\`            |  `"Look, a mountain: /\\"` |  `Look, a mountain: /\` |
| `\n`         |                |   `"1\n2 3"`               |   `1`<br>`2 3`              |

- String methods: `.upper()`, `.lower()`, `.index()`, `.startswith()`
    - besides using `.format()`, [f-strings](https://realpython.com/python-f-strings/) also allows using variables inside strings to build dynamic messages.

- conversion to/from lists: `.join()`, `.split()`
- `str()`
- [Exercises](https://runestone.academy/runestone/books/published/thinkcspy/Strings/Exercises.html)

#### Dictionaries [cheatsheet (dictionary)](https://drive.google.com/file/d/1H_OP3ENYKB3A-h_dSGRwhjKz1DydtYko/view?usp=sharing)
> Dictionaries store connections between pieces of information. Each item in a dictionary is a **key-value** pair.

- dictionary comprehension
- looping over a dictionary with methods: `.keys()`, `.values()`, `.items()`
- [Exercises](https://runestone.academy/runestone/books/published/thinkcspy/Dictionaries/Exercises.html)
---

### 1.1.7 Working with External Libraries
- `import __ as _`
- `from __ import *`
- importing `math` and `numpy`
- operator overloading
- using [datetime](https://www.freecodecamp.org/news/how-to-use-timedelta-objects-in-python/)
   - The datetime library will be particularly useful when we have to deal with time later on Quantconnect

#### installing python libraries with `pip`
In module 2, you will have to install machine learning and data science libraries. Here's how to do it.
- [How to download and install Python Packages and Modules with Pip](https://www.youtube.com/watch?v=jnpC_Ib_lbc)
---

## Optional Resources
If you want to explore more before moving onto Object-Oriented Programming, you might be interested in:
[Beginner resources - Python resources for everybody](https://learnbyexample.github.io/py_resources/beginners.html)
- a list of good python learning materials and tips and where to get help

[How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/runestone/books/published/thinkcspy/index.html)
- gives you a solid foundation to programming, teaches debugging right at the beginning, includes case studies, exercises, etc
- based on the book ["Think Python"](https://greenteapress.com/wp/think-python/)


[Programming with Mosh - Python for Beginners [Full Course]](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
- A full course on python basics, if you do not feel like reading text-based guides you can learn the entire module 1a and 1b by following along this video

---

## Common Beginner Errors
Beginners may have trouble dealing with exceptions and errors. Here is a handy flowchart from https://pythonforbiologists.com for troubleshooting errors

[HD version](https://drive.google.com/file/d/1gJC-NfMGdQpWEcivOMfOCzIJZLSVKb-b/view?usp=sharing)

![cmn problems](http://i.imgur.com/WRuJV6rl.png)

---

## Next Up:

You will learn [Object Oriented Programming](<./Module 1.2 Object Oriented Programming.md>) in Python 3.

---

## References

- [Python tutorials - Kaggle](https://www.kaggle.com/learn/python)
- [How to teach yourself hard things](https://jvns.ca/blog/2018/09/01/learning-skills-you-can-practice/)
- [f-strings](https://realpython.com/python-f-strings/)
- [Python Crash Course 2nd Edition Cheatsheets](https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/)
- [datetime - freeCodeCamp](https://www.freecodecamp.org/news/how-to-use-timedelta-objects-in-python/)
- [How to download and install Python Packages and Modules with Pip](https://www.youtube.com/watch?v=jnpC_Ib_lbc)
- [Beginner resources - Python resources for everybody](https://learnbyexample.github.io/py_resources/beginners.html)
- [How to Think Like a Computer Scientist: Interactive Edition](https://runestone.academy/runestone/books/published/thinkcspy/index.html)
- ["Think Python"](https://greenteapress.com/wp/think-python/)
- [Programming with Mosh - Python for Beginners [Full Course]](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
- [Common beginner problems - python for biologists](https://pythonforbiologists.com)
