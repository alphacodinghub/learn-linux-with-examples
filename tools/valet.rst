.. _valet:

Valet Quick Start on Ubuntu
=============================

.. note:: We assume the Linux variation is Ubuntu /pop!_os.

Valet Installation
-------------------
Insatall packages: php, composer, node, npm; Valet; mariadb; laravel.

From a terminal, run the following commands for initial settings::

  $ cd ~
  $ mkdir Sites
  $ cd Sites
  $ valet domain dev
  $ valet park

Install mariadb & phpMyAdmin
------------------------------
**Install mariadb**::

  sudo apt install mariadb-server

By default, the root password is empty. 
There is a bug when you try to login mysql without sudo::

  mysql -uroot

To fix this::

  sudo mysql -uroot
  use mysql;
  update user set plugin='' where user='root';
  flush privileges;
  \q

Now, you can log into mysql without sudo::

  mysql -uroot
  show variables like "%version%";

The output of the above command looks like::

  +-----------------------------------+------------------------------------------+
  | Variable_name                     | Value                                    |
  +-----------------------------------+------------------------------------------+
  | in_predicate_conversion_threshold | 1000                                     |
  | innodb_version                    | 10.3.22                                  |
  | protocol_version                  | 10                                       |
  | slave_type_conversions            |                                          |
  | system_versioning_alter_history   | ERROR                                    |
  | system_versioning_asof            | DEFAULT                                  |
  | version                           | 10.3.22-MariaDB-1ubuntu1                 |
  | version_comment                   | Ubuntu 20.04                             |
  | version_compile_machine           | x86_64                                   |
  | version_compile_os                | debian-linux-gnu                         |
  | version_malloc_library            | system                                   |
  | version_source_revision           | 0152704ae3f857668dbc05803950adcf131b8685 |
  | version_ssl_library               | YaSSL 2.4.4                              |
  | wsrep_patch_version               | wsrep_25.24                              |
  +-----------------------------------+------------------------------------------+

**Insatall phpMyAdmin**

- Downloaded phpmyadmin via https://www.phpmyadmin.net/
- Unzipped the file, moved the directory to my Valet park directory (`~/Sites`), and renamed the directory "phpMyAdmin"
- Now, visiting http://phpmyadmin.dev should work. However mariadb does not have a password by default for phpMyAdmin to work. To set a password, run the following commands from a terminal::
    
    mysql -uroot
    SET PASSWORD FOR 'root'@'localhost' = PASSWORD('root');
    \q

  This will set username (`root`) with the password (`root`). Now you can log into the db like this::

    mysql -uroot -proot
    SHOW DATABASES;
    \q

- You can log into mariadb DB server from the web UI with username (`root`) and password (`root`).

.. important:: 
  If you don't want to move the extracted phpMyAdmin files to the Valet park directory, you can link the directory to Valet park directory.

  For example, if the directory is `/usr/local/share/phpmyadmin`, do the following::

    cd /usr/local/share/phpmyadmin
    valet link

  visit: `http://phpmyadmin.dev` to manage the db.