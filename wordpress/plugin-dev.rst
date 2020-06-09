.. _pluginDev:

Create a WordPress Plugin from Scratch
========================================

Plugin folder structure
------------------------
WordPress plugins are normally located in the `wp-content` folder of the WordPress root folder.

This is the folder structure of Plugin Akismet Anti-Spam::

  akismet   <--- Plugin main folder
  ├── akismet.php   <--- Plugin main file
  ├── changelog.txt
  ├── class.akismet-admin.php
  ├── class.akismet-cli.php
  ├── class.akismet.php
  ├── class.akismet-rest-api.php
  ├── class.akismet-widget.php
  ├── _inc
  │   ├── akismet.css
  │   ├── akismet.js
  │   ├── form.js
  │   └── img
  │       └── logo-full-2x.png
  ├── index.php
  ├── LICENSE.txt
  ├── readme.txt
  ├── views
  │   ├── activate.php
  │   ├── config.php
  │   ├── connect-jp.php
  │   ├── enter.php
  │   ├── get.php
  │   ├── notice.php
  │   ├── predefined.php
  │   ├── setup.php
  │   ├── start.php
  │   ├── stats.php
  │   └── title.php
  └── wrapper.php

In the main php file of a plugin, standard infomation of the plugin and its copyright declaration should be placed.

.. code-block:: php

  <?php
  /**
  * @package Akismet
  */
  /*
  Plugin Name: Akismet Anti-Spam
  Plugin URI: https://akismet.com/
  Description: Used by millions, Akismet is quite possibly the best way in the world to <strong>protect your blog from spam</strong>. It keeps your site protected even while you sleep. To get started: activate the Akismet plugin and then go to your Akismet Settings page to set up your API key.
  Version: 4.1.5
  Author: Automattic
  Author URI: https://automattic.com/wordpress-plugins/
  License: GPLv2 or later
  Text Domain: akismet
  */

  /*
  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

  Copyright 2005-2015 Automattic, Inc.
  */

To secure WordPress development
---------------------------------
As a security measure, normal users should be prevented from access to any folder or php file directly. The standard practice for WordPress development is to:

- Place an empty `index.php` file in folders where there is no actual functioning `index.php` existed:

  .. code-block:: php

    //file: index.php

    <?php
    // Silence is golden.

- Place some code at the beginning of php files.

  For example:

  .. code-block:: php

    defined( 'ABSPATH' ) or die( 'Hey, you can\'t access this file, you silly human!' );

  or

  .. code-block:: php

    if ( ! function_exists( 'add_action' ) ) {
      echo 'Hey, you can\t access this file, you silly human!';
      exit;
    }

Start up plugin development - alecaddd plugin
-----------------------------------------------
Create folder `alecaddd` under `wp-content`, and generate two files as below::

  alecaddd    <--- plugin main folder
  ├── alecaddd-plugin.php    <--- plugin main file
  └── index.php   <--- empty file

Using OOP method to programme
---------------------------------
Object-Oriented Programming naming convention:

- File name: all lower case, dash seperated, e.g. alecaddd-plugin.php
- Class: Pascal, e.g. `class AlecadddPlugin`
- Methods and functions: all lower case, uderscore seperated, e.g. register_activation_hook()
- Variables: camel, e.g. alecadddPlugin

.. index:: register_activation_hook, register_deactivation_hook

e.g.:

.. code-block:: php

  //file: alecaddd-plugin.php

  defined( 'ABSPATH' ) or die( 'Hey, what are you doing here? You silly human!' );

  class AlecadddPlugin
  {
    function __construct() {
      add_action( 'init', array( $this, 'custom_post_type' ) );
    }

    function activate() {
      // generated a CPT
      $this->custom_post_type();
      // flush rewrite rules
      flush_rewrite_rules();
    }

    function deactivate() {
      // flush rewrite rules
      flush_rewrite_rules();
    }

    function uninstall() {
      // delete CPT
      // delete all the plugin data from the DB
    }

    function custom_post_type() {
      register_post_type( 'book', array( 'public' => true, 'label' => 'Books' ) );
    }
  }

  if ( class_exists( 'AlecadddPlugin' ) ) {
    $alecadddPlugin = new AlecadddPlugin();
  }

  // activation
  register_activation_hook( __FILE__, array( $alecadddPlugin, 'activate' ) );

  // deactivation
  register_deactivation_hook( __FILE__, array( $alecadddPlugin, 'deactivate' ) );

To register the plugin activation and deactivation hook::

  // activation
  register_activation_hook( __FILE__, array( $alecadddPlugin, 'activate' ) );

  // deactivation
  register_deactivation_hook( __FILE__, array( $alecadddPlugin, 'deactivate' ) );

To register Custom Post Type
------------------------------
This is added to class __construct() function:

.. index:: add_action, register_post_type

.. code-block:: php

  //file: alecaddd-plugin.php

  class AlecadddPlugin
  {
    function __construct() {
      add_action( 'init', array( $this, 'custom_post_type' ) );
    }

    function custom_post_type() {
      register_post_type( 'book', array( 'public' => true, 'label' => 'Books' ) );
    }
  }



