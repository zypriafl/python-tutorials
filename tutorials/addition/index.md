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
---

# Know your tools

Programming is an art of balancing simplicity and complexity. But there is a peculiar attraction to complexity that we as developers often fall into. Let's dive into this complexity trap, look at some common tasks and see how they can be overcomplicated in non-optimal ways.

```{contents} Table of Contents
:depth: 3
```

## Addition of two numbers

The easy way:

```{code-cell}
def add(x, y):
    return x + y
```

```{code-cell}
add(1, 1)
```


```{admonition} Note
In the second example, the developer is trying to implement a bitwise addition algorithm. It's a fascinating concept, but it's overkill for this basic task and can lead to problems like infinite loops when dealing with negative numbers or floating point numbers.
```

```{code-block}
def add(x, y):
    if y == 0:
        return x
    else:
        return add(x ^ y, (x & y) << 1)
```

## Lessons from the trap

```{tip}
Overcomplicating tasks doesn't make you a better programmer. Instead, it can make your code harder to understand, harder to maintain, and more prone to bugs. Here are some takeaways that can help you avoid the complexity trap:
```


Know your tools: Modern programming languages have a large number of built-in Functions and Libraries, which are designed to make your life easier. Use them.
Keep it simple: The best solution is often the simplest. Avoid unnecessary loops, recursions or bit operations if a straightforward solution is available.
Readability counts: Code is read more often than it is written. Make sure your code is clean and easy to understand.
Test your code: Testing always use your code, especially if you have a complex algorithm try out. This helps to detect bugs and performance problems at an early stage.
Contact an expert for a Python trainingOften the experience of experts helps to accelerate one's own learning curve.
Remember, the goal of coding is not to create complex algorithms that only you can understand, but to solve problems in the most efficient and maintainable way. Be aware of th