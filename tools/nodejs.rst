.. _nodejs:

The bellow is from Sousa's blog: `Switching between Node versions during development <https://blog.logrocket.com/switching-between-node-versions-during-development/>`_.

Manage Node versions on Linux and Mac
======================================
Sometimes it seems like there are new versions of Node.js released almost weekly — minor versions every few weeks, major versions every few months. If you are a developer that needs to switch between different applications and projects on a regular basis, you may find you need to run different versions of Node.

Luckily, there are several decent ways to install multiple versions and switch as needed. This article will discuss and compare two popular Node version managers: NVM for Windows and the n Node version manager for Linux/Mac.

n Node version manager
------------------------
The n Node version manager provides a simpler CLI for installing and switching between Node versions. It is only supported on Linux or Mac operating systems.

`Details on github <https://github.com/tj/n>`_

Installation
^^^^^^^^^^^^^^^^^^
If you have a version of Node and npm installed already, you can install n just like any other NPM package using::

  npm install -g n

If you don’t already have a version of Node or npm installed, you can install n with a bash script from GitHub. Here is what it looks like:

.. tip:: You must have Git installed to install n with the bash script.

::

  ~$ curl -L https://git.io/n-install | bash
  ...
  === n successfully installed.
    The active Node.js version is: v10.16.0

    Run `n -h` for help.
    To update n later, run `n-update`.
    To uninstall, run `n-uninstall`.
  ===
  ~$ source ~/.bashrc
  ~$ n
  node/10.16.0

.. IMPORTANT:: 
  After installing `n`, open a new terminal or run `source ~/.bashrc` before using n and Node.js.

The `n` command for installing and activating a version of Node is simple::

  n 11.15.0     # install and activate Node version 11.15.0
  n latest      # latest version
  n latest      # latest LTS version

If the version of Node is already installed, then n will simply switch to that version.

After installing Node, the application can be run as usual::

  node --version

  npm install

NVM for Windows
=================
Technically, there are two completely separate NVM projects that offer similar capabilities on different operating systems but are maintained independent of each other:

nvm-sh/nvm is a bash script that can be used to manage Node versions on Linux and Mac

coreybutler/nvm-windows is a Windows application (with or without an installer) that can be used to managed Node versions on Windows

