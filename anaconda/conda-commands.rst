.. _condaCommands:

Conda Commands
================
Main Conda Commands:

======================================  ==========================================
Task                                    Conda command
======================================  ==========================================
Install a package                       `conda install $PKG_NAME`
Update a package                        `conda update --name $ENV_NAME $PKG_NAME`
Update package manager                  `conda update conda`
Uninstall a package                     `conda remove --name $ENV_NAME $PKG_NAME`
Create an environment                   `conda create --name $ENV_NAME python`
Activate an environment                 `conda activate $ENV_NAME`
Deactivate an environment               `conda deactivate`
Search available packages               `conda search $SEARCH_TERM`
Install package from specific source    `conda install --channel $URL $PKG_NAME`
List installed packages                 `conda list --name $ENV_NAME`
Create requirements file                `conda list --export`
List all environments                   `conda info --envs`
Install other package manager           `conda install pip`
Install Python                          `conda install python=x.x`
Update Python                           `conda update python`
======================================  ==========================================

References
==============

#. `Command reference <https://conda.io/projects/conda/en/latest/commands.html>`_
#. `Conda Cheat Sheet <https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html>`_
#. `Anaconda Documentation <https://docs.anaconda.com/>`_