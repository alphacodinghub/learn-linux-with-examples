.. _sphinxQuickStart:

About Sphinx
==============
Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.

It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

Features
---------

#. **Output formats:** HTML (including Windows HTML Help), LaTeX (for printable PDF versions), ePub, Texinfo, manual pages, plain text
#. **Extensive cross-references:** semantic markup and automatic links for functions, classes, citations, glossary terms and similar pieces of information
#. **Hierarchical structure:** easy definition of a document tree, with automatic links to siblings, parents and children
#. **Automatic indices:** general index as well as a language-specific module indices
#. **Code handling:** automatic highlighting using the Pygments highlighter
#. **Extensions:** automatic testing of code snippets, inclusion of docstrings from Python modules (API docs), and more
#. **Contributed extensions:** more than 50 extensions contributed by users in a second repository; most of them installable from PyPI

Install Sphinx
================
Using the following command to install Sphinx::

  pip install -U Sphinx

Set up the documentation sources
=================================
To set up the documentation sources, run::

  sphinx-quickstart

Follow the prompts to complete the settings. It will create a source directory with `conf.py` and a master document, `index.rst`.

Useful commands::

  make html
  make man
  make epub

To use live build html function, install sphinx-autobuild::

  pip install sphinx-autobuild

You can then use this command to automatically generate html whenever source files change::

  sphinx-autobuild src dest

where `src` is the main source file (index.rst or content.rst) folder, `dest` is the `html` folder. e.g.::

  sphinx-autobuild  .  _build/html
  # sphinx will monitor source files in the current folder and build html automatically.
  

Documents
================

#. `Sphinx Quick Start <https://www.sphinx-doc.org/en/master/usage/quickstart.html#id7>`_
#. `Sphinx Extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_