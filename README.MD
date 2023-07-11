# MyST, MyST-NB, Jupytext, and Sphinx Tutorial

This repository shows how to use 

- [MyST](https://myst-parser.readthedocs.io/en/latest/)
- [MyST-NB](https://myst-nb.readthedocs.io/en/latest/)
- [Jupytext](https://jupytext.readthedocs.io/en/latest/)
- [Sphinx](https://www.sphinx-doc.org/en/master/) for your documentation workflow.

## Setup

To start with, install the necessary dependencies via pip:

`pip install -r requirements.txt`

Sphinx
------

Sphinx is a powerful documentation generator that converts reStructuredText files into HTML websites and other formats including PDF, EPub, and more.

You need to create a configuration file named `conf.py` in the root directory of your project where you specify the configuration of your Sphinx documentation.

To quickly generate a default `conf.py`, use:

`sphinx-quickstart`

And follow the prompts.

MyST
----

MyST is a markdown parser that allows you to write Sphinx documentation in markdown. To use MyST, you need to add the following lines to your `conf.py`:

`extensions = [
    ...
    'myst_parser',
]`

MyST-NB
-------

MyST-NB is an extension to MyST that enables parsing of Jupyter notebooks. To use MyST-NB, add the following to your `conf.py`:

`extensions = [
    ...
    'myst_nb',
]`

Jupytext
--------

Jupytext is a Jupyter plugin that reads and writes notebooks in various text-based file formats. It allows you to version control Jupyter notebooks effectively.

Jupytext pairs your notebook with a `.md` (or other formats) such that changes in either the `.ipynb` or `.md` file are reflected in the other. To pair a notebook with a markdown file, you can use the Jupytext command in the command line:

`jupytext --set-formats ipynb,md:myst notebook.ipynb`

Building the Documentation
--------------------------

Once everything is set up, you can build your documentation with Sphinx using:

`sphinx-build -b html . public  `

This will generate a `public/html` directory with your built documentation.

Including Notebooks in Your Documentation
-----------------------------------------

To include notebooks in your Sphinx documentation, add them to your toctree directive in your `index.md` (or `index.rst`) file:

markdownCopy code

```{toctree}
:maxdepth: 2
:caption: Contents:

tutorials/nan-values/index.md
```

The `index` file here refers to `tutorials/nan-values/index.md`.

One directory is used per tutorials to ensure all assets are contained in this folder. In addition, it helps to 
keep the url clean, which means the URL is `HOST/tutorials/nan-values/` instead of `HOST/tutorials/nan-values.html`.

Enjoy documenting your project!