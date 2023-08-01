---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Recursion

```{code-cell} ipython2
def f(x):
    if x == 0:
        return x
    else:
        return f(x-1)
```

```{code-cell} ipython2
f(10) 
```

```{raw-cell}
This function always return 0 for positive Numbers. Can you guess what happens for negative numbers?
```
