.. _miniconda:

Miniconda
============
Miniconda is a free minimal installer for conda. It is a small, bootstrap version of Anaconda that includes only conda, Python, 
the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. Use the `conda install command` to install 720+ additional conda packages from the Anaconda repository.

.. note:: *Miniconda is right for you if you:*

  - Do not mind installing each of the packages you want to use individually.
  - Do not have time or disk space to install over 1,500 packages at once.
  - Want fast access to Python and the conda commands and you wish to sort out the other programs later.

Installing on Linux
---------------------
Follow the below steps to install miniconda on Linux:

1. Download the installer: `Miniconda download link <https://docs.conda.io/en/latest/miniconda.html>`_
#. Verify the installer hashes
#. Run the following command in your terminal window:

  .. code-block:: bash

    bash Miniconda3-latest-Linux-x85_64.sh

4. Follow the prompts on the installer screens.
#. When installation is completed, re-load the terminal window to make the changes take effect.
#. Run the command `conda list` to test the installation. Congratualations if you see a list of installed packages listed!

Updating
-----------------
To update Miniconda or Anaconda, run the command in a terminal window::

  conda update conda

Uninstalling Miniconda
------------------------------------
To remove the entire Miniconda, run the command in a terminal window::

  rm -rf ~/miniconda

.. admonition:: And, by the way...
  
  Please refer to :ref:`condaCommands` for how to use conda.
  