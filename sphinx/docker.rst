.. _sphinxDocker:

Docker Sphinx
===============

Docker Images
---------------

- alphacodinghub/sphinx-latexpdf

.. note::
  This image is based on the official image and added more support for languages and themes. The official image does not work very well (lack of some packages) for pdf.

Usages
-----------

.. code-block:: bash

  $ docker run --rm -v /path/to/document:/docs alphacodinghub/sphinx sphinx-quickstart

.. info:: This may not work properly as command `sphinx-quickstart` requires 
  input from stdin. It is recommended to loginto the docker container to run commands.

if you work in the current directory, you can use::

  $ docker run --rm -v $PWD:/docs alphacodinghub/sphinx-latexpdf sphinx-quickstart

To access to the Docker container::

  $ docker run --rm -it -v $PWD:/docs alphacodinghub/sphinx-latexpdf bash
  then run sphinx commands, e.g.
  $ sphinx-quickstart
  or
  $ make html
  or
  $ make epub
  or
  $ make latexpdf

Build HTML document::

  $ docker run --rm -v /path/to/document:/docs alphacodinghub/sphinx-latexpdf make html

Build EPUB document::

  $ docker run --rm -v /path/to/document:/docs alphacodinghub/sphinx-latexpdf make epub

Build PDF document::

  $ docker run --rm -v /path/to/document:/docs alphacodinghub/sphinx-latexpdf make latexpdf


References
================

#. `Sphinx Docker images <https://hub.docker.com/r/sphinxdoc/sphinx-latexpdf>`_
#. `Sphinx Docker image by David DIDIER <https://gitlab.com/ddidier/docker-sphinx-doc>`_