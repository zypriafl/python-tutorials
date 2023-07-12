# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Python Tutorials'
copyright = '2023, Helm & Nagel GmbH'
author = 'Christopher Helm'
html_title = 'Python Tutorials'
# The full version, including alpha/beta/rc tags
release = '0.1.0'
html_baseurl  = 'https://atraining.github.io/python-tutorials/'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "jupyter_execute\*", "**.ipynb_checkpoints", "venv/*"]
# Very important, exclude your venv directory, otherwise you might receive:
# raise DeadKernelError("Kernel died")
# thanks to https://github.com/executablebooks/jupyter-book/issues/1918#issuecomment-1440833493


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'

# Setup the notebook execution for mystnb.config
# nb_execution_mode = "off"
nb_execution_timeout = -1  # no execution timeout in seconds
nb_execution_raise_on_error = True  # Raise an exception on failed execution, rather than emitting a warning
# To trigger the execution of notebook pages, use the following configuration in conf.py:
nb_execution_mode = "auto"  # by https://myst-nb.readthedocs.io/en/v0.9.1/use/execute.html

# These folders are copied to the documentation's HTML output
# html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# The master toctree document.
master_doc = 'index'
