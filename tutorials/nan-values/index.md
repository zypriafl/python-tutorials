---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
mystnb:
  execution_timeout: 60
---

# NaN Values

## Introduction
NaN (Not a Number) values are ubiquitous in data science, often used to represent missing or undefined data.
In this tutorial, we will learn how to handle NaN values in Python using numpy and pandas libraries.

```{contents} Table of Contents
:depth: 3
```

## Prerequisites
Basic Python knowledge, basic understanding of numpy and pandas libraries. Make sure you have numpy and pandas installed in your Python environment.

## Importing Necessary Libraries
Let's start by importing necessary libraries.

```{code-cell}
import numpy as np
import pandas as pd
```
Creating NaN values
Let's create a numpy array and a pandas DataFrame containing NaN values.

```{code-cell}
nan_array = np.array([1, 2, np.nan, 4, 5])
nan_df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5]
})
nan_df
```

## Arithmetic Operations with NaN
Now we can see how NaN values affect arithmetic operations. For example, if we try to calculate the mean of the numpy array, we will get a NaN result

```{code-cell}
print("Mean of numpy array:", np.mean(nan_array))
```
This is because any arithmetic operation with NaN results in NaN. We can avoid this by using the np.nanmean function instead, which ignores NaN values

```{code-cell}
print("Mean of numpy array ignoring NaN:", np.nanmean(nan_array))
```

```{code-cell}
assert np.nanmean(nan_array) == 3, 'np.nanmean did not work correctly!'
```
In pandas, the mean function automatically ignores NaN values

```{code-cell}
:tags: [hide-cell]
print("Mean of pandas DataFrame columns:\n", nan_df.mean())
```

Use `:tags: [remove-input, remove-output]` in a `{code-cell}` to include assert statements to make sure everything 
is working as expected.

Let's say we want to render the following cell:

```
\```{code-cell}
:tags: [remove-input, remove-output]
assert nan_df.mean().equals(pd.Series({'A': 3, 'B': 3.5})), 'pandas mean function did not work correctly!'
\```
```

start of the output
```{code-cell}
:tags: [remove-input, remove-output]
assert nan_df.mean().equals(pd.Series({'A': 3, 'B': 3.5})), 'pandas mean function did not work correctly!'
```
end of the output

Find out more how to `hide-` or `remove-´ output [here](https://myst-nb.readthedocs.io/en/latest/render/hiding.html#remove-parts-of-cells).

Use `:tags: [raises-exception]` if you want to show an error on purpose. Any other Exception will stop the documentation
build process, as we force to `nb_execution_raise_on_error = True` in the `conf.py`.

```{code-cell} ipython3
:tags: [raises-exception]

raise ValueError("oopsie! ")
```


## Conclusion

In summary, handling NaN values is important when working with data in Python. NaN values can impact the results of arithmetic operations. Both numpy and pandas provide functions to handle NaN values effectively.

