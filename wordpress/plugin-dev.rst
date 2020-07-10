.. _pluginDev:

Create a WordPress Plugin from Scratch
========================================

This tutorial is based on the Alessandro Castellani's youtube toturials: https://youtu.be/0l7JTie_6jM

The full source code is availabel on github: https://github.com/webazad/alecaddd-plugin

Full list of sections and features we will build during the series of Tutorials

* Modular Administration Area
* CPT Manager
* Custom Taxonomy Manager
* Widget to Upload and Diaply media in sidebars
* Post and Pages Gallery integration
* Testimonial section: Comment in the front-end, ADmins can approve comments, select which comments to display
* Custom template sections
* Ajax based Login/Register system
* Membership protected area
* Chat system

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
  <?php
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

Register Custom Post Type
------------------------------
This is added to class __construct() function:

.. index:: add_action, register_post_type

.. code-block:: php
  :linenos:

  //file: alecaddd-plugin.php
  <?php

  class AlecadddPlugin
  {
    function __construct() {
      add_action( 'init', array( $this, 'custom_post_type' ) );
    }
  // ...
    function custom_post_type() {
      register_post_type( 'book', array( 'public' => true, 'label' => 'Books' ) );
    }
  }

Uninstall Plugin
--------------------

When a plugin is deactivated from the WP Dashboard, WP will run the `uninstall.php` file in the plugin root directory if there is such a `uninstall.php` file. You can clean up the database when the plugin is removed.

You can use WP functions or mysql query to delete records from database.

.. index:: get_posts, wp_delete_post

.. code-block:: php
  :linenos:   
  :emphasize-lines: 15, 18

  // file: uninstall.php
  <?php

  /**
  * Trigger this file on Plugin uninstall
  *
  * @package  AlecadddPlugin
  */

  if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
    die;
  }

  // Clear Database stored data
  $books = get_posts( array( 'post_type' => 'book', 'numberposts' => -1 ) );

  foreach( $books as $book ) {
    wp_delete_post( $book->ID, true );
  }

  // Access the database via SQL
  global $wpdb;
  $wpdb->query( "DELETE FROM wp_posts WHERE post_type = 'book'" );
  $wpdb->query( "DELETE FROM wp_postmeta WHERE post_id NOT IN (SELECT id FROM wp_posts)" );
  $wpdb->query( "DELETE FROM wp_term_relationships WHERE object_id NOT IN (SELECT id FROM wp_posts)" );

Enqueue Admin Scripts
-----------------------
In order to use customised js and css, we need to enqueue these files using WP functions:

| css:  wp_enqueue_style( )
| js:   wp_enqueue_script( )

We also need to call `add_action()` to load scripts at appropriate times:

| add_action('admin_enqueue_scripts', array()): to load for **Admin** (backend)
| add_action('wp_enqueue_scripts', array()): to load for **Users** (frontend)

.. code-block:: php

  <?php

  if ( !class_exists( 'AlecadddPlugin' ) ) {

    class AlecadddPlugin
    {
      function register() {
        add_action( 'admin_enqueue_scripts', array( $this, 'enqueue' ) );
      }
      
      function enqueue() {
        // enqueue all our scripts
        wp_enqueue_style( 'mypluginstyle', plugins_url( '/assets/mystyle.css', __FILE__ ) );
        wp_enqueue_script( 'mypluginscript', plugins_url( '/assets/myscript.js', __FILE__ ) );
      }      
    }

    $alecadddPlugin = new AlecadddPlugin();
    $alecadddPlugin->register();
  }

Admin Pages and Settings Link
--------------------------------

**Add admin menus and pages to Dashboard**

.. _add-admin-pages:

To add menu item and related pages to Dashboard, do the following:

- Call `add_action('admin_menu', array( $this, 'add_admin_pages' ))` to hook a function, here `add_admin_pages` to add menus and pages;
- In the function `add_admin_pages` to call `add_menu_page()` and `add_submenu_page()` to actually add menus and pages.

.. index:: add_menu_page, add_submenu_page

For details on relevant functions:

- `add_menu_page() <https://developer.wordpress.org/reference/functions/add_menu_page/>`_
- `add_submenu_page() <https://developer.wordpress.org/reference/functions/add_menu_page/>`_
- `add_action('admin_menu', string) <https://developer.wordpress.org/reference/hooks/admin_menu/>`_
- `Dashicons <https://developer.wordpress.org/resource/dashicons/>`_

Example of adding menus and pages to Dashboard:

.. code-block:: php

  <?php 
  class Admin
  {
    public function register() {
      add_action( 'admin_menu', array( $this, 'add_admin_pages' ) );
    }

    public function add_admin_pages() {
      add_menu_page( 'Alecaddd Plugin', 'Alecaddd', 'manage_options', 'alecaddd_plugin', array( $this, 'admin_index' ), 'dashicons-store', 110 );
    }

    public function admin_index() {
      require_once PLUGIN_PATH . 'templates/admin.php';
    }
  }

**Add Settings Link for Plugin**

Using filter `plugin_action_links_` to add settings_link.

Details for the filter:

`add_filter("plugin_action_links_NAME_OF_THE_LINK", string) <https://codex.wordpress.org/Plugin_API/Filter_Reference/plugin_action_links_(plugin_file_name)>`_

Example: 

.. code-block:: php
  :linenos:
  :emphasize-lines: 6

  <?php
  class SettingsLinks extends BaseController
  {
    public function register() 
    {
      add_filter( "plugin_action_links_$this->plugin", array( $this, 'settings_link' ) );
    }

    public function settings_link( $links ) 
    {
      $settings_link = '<a href="admin.php?page=alecaddd_plugin">Settings</a>';
      array_push( $links, $settings_link );
      return $links;
    }
  }

To determine the `url` of the link as in the above `href="admin.php?page=alecaddd_plugin"`:

- To add the admin pages first as described in the :ref:`above <add-admin-pages>`.
- Visit the added admin page and get the link url in the browser's address bar.

.. note::
  The BaseController class contains some public variables used in its extened classes. It is defined as:

  .. code-block:: php

    <?php 
    /**
    * @package  AlecadddPlugin
    */
    namespace Inc\Base;

    class BaseController
    {
      public $plugin_path;

      public $plugin_url;

      public $plugin;

      public function __construct() {
        $this->plugin_path = plugin_dir_path( dirname( __FILE__, 2 ) );
        $this->plugin_url = plugin_dir_url( dirname( __FILE__, 2 ) );
        $this->plugin = plugin_basename( dirname( __FILE__, 3 ) ) . '/alecaddd-plugin.php';
      }
    }

Using Composer
-----------------
Composer can auto load php files.

- Install Composer
- In the plugin root directory, run::

    composer init
    composer install

This will generate required files.

we add "autoload" statement to the end of the generated json file `composer.json`, which now looks like:

.. code-block:: json

  {
      "name": "alecaddd/alecaddd-plugin",
      "description": "Awesome starter plugin example",
      "type": "project",
      "license": "GPL",
      "authors": [
          {
              "name": "Alecaddd",
              "email": "castellani.ale@gmail.com"
          }
      ],
      "minimum-stability": "dev",
      "require": {},
      "autoload": {
          "psr-4": {"Inc\\": "./inc"}
      }
  }

In the json file, we can see that we used "psr-4" convention, and the namespace "Inc". Files under this namespace will be autoloaded. `./inc` is the directory that the "Inc" namespace points to.

If we change the namespace, say "Ale",  we need to run the bellow command to re-generate autoloading files::

  composer dump-autoload

In order to use this autoloading feature, we need to `require_once` the `autoload.php` file in the main plugin file (`alecaddd-plugin.php`) and include namespaces:

.. code-block:: php

  <?php
  if ( file_exists( dirname( __FILE__ ) . '/vendor/autoload.php' ) ) {
    require_once dirname( __FILE__ ) . '/vendor/autoload.php';
  }

  use Inc\Activate;
  use Inc\Deactivate;
  use Inc\Admin\AdminPages;

  if ( !class_exists( 'AlecadddPlugin' ) ) {
  //...

.. important:: Naming convention should be followed - File names and Class names should match each other.
  e.g. file `./inc/Activate.php` has the content:

  .. code-block:: php

    <?php
    /**
    * @package  AlecadddPlugin
    */
    namespace Inc;

    class Activate
    {
      public static function activate() {
        flush_rewrite_rules();
      }
    }

  The file name is `Activate.php` and the class name is `Activate`.

The plugin folder structure now looks like::

  alecaddd
  ├── alecaddd-plugin.php
  ├── assets
  │   ├── myscript.js
  │   └── mystyle.css
  ├── composer.json
  ├── inc       <--- namespace Inc
  │   ├── Activate.php
  │   ├── Admin     <--- namespace Inc\Admin
  │   │   └── AdminPages.php
  │   └── Deactivate.php
  ├── index.php
  ├── templates
  │   └── admin.php
  ├── uninstall.php
  └── vendor
      ├── autoload.php
      └── composer
          ├── autoload_classmap.php
          ├── autoload_namespaces.php
          ├── autoload_psr4.php
          ├── autoload_real.php
          ├── autoload_static.php
          ├── ClassLoader.php
          ├── installed.json
          └── LICENSE

  6 directories, 19 files

Restructure and Clean up
--------------------------
Now, we use namespace, static method, composer autoload. We can restructure the plugin and files in a  concise way. The new structure::

  alecaddd
  ├── alecaddd-plugin.php
  ├── assets
  │   ├── myscript.js
  │   └── mystyle.css
  ├── composer.json
  ├── inc
  │   ├── Base
  │   │   ├── Activate.php
  │   │   ├── BaseController.php
  │   │   ├── Deactivate.php
  │   │   ├── Enqueue.php
  │   │   └── SettingsLinks.php
  │   ├── Init.php
  │   └── Pages
  │       └── Admin.php
  ├── index.php
  ├── templates
  │   └── admin.php
  ├── uninstall.php
  └── vendor
      ├── autoload.php
      └── composer
          ├── autoload_classmap.php
          ├── autoload_namespaces.php
          ├── autoload_psr4.php
          ├── autoload_real.php
          ├── autoload_static.php
          ├── ClassLoader.php
          ├── installed.json
          └── LICENSE

  7 directories, 23 files

Modular Adminstration Page (Part 14)
-------------------------------------

.. index:: Wordpress Settings API, register_setting, add_settings_field, add_settings_section

Please refer to `WordPress Settings API <https://codex.wordpress.org/Settings_API>`_ for more details.

Running sequence:

1. alecaddd.php: registrate activation & deactivation hooks -> call Inc\\Init in ./inc/Init.php file
#. ./inc/Init.php: call register_services() to register services (i.e. classes) in: 
  
    - ./inc/Pages/Admin.php: **Modular Administration Page**
    - ./inc/Base/Enqueue.php: enqueue css and js scripts
    - ./inc/Base/SettingsLinks.php: setting plugin Settings link

Admin.php uses SettingsApi.php to realise modularised Administration Page.

Amin.php code:

.. code-block:: php
  :linenos:

  <?php 
  /**
  * @package  AlecadddPlugin
  */
  namespace Inc\Pages;

  use \Inc\Base\BaseController;
  use \Inc\Api\SettingsApi;

  /**
  * 
  */
  class Admin extends BaseController
  {
    public $settings;

    public $pages = array();

    public function __construct()
    {
      $this->settings = new SettingsApi();

      $this->pages = array(
        array(
          'page_title' => 'Alecaddd Plugin', 
          'menu_title' => 'Alecaddd', 
          'capability' => 'manage_options', 
          'menu_slug' => 'alecaddd_plugin', 
          'callback' => function() { echo '<h1>Alecaddd Plugin</h1>'; }, 
          'icon_url' => 'dashicons-store', 
          'position' => 110
        )
      );
    }

    public function register() 
    {
      $this->settings->addPages( $this->pages )->register();
    }
  }

SettingsApi.php code:

.. code-block:: php
  :linenos:

  <?php 
  /**
  * @package  AlecadddPlugin
  */
  namespace Inc\Api;

  class SettingsApi
  {
    public $admin_pages = array();

    public function register()
    {
      if ( ! empty($this->admin_pages) ) {
        add_action( 'admin_menu', array( $this, 'addAdminMenu' ) );
      }
    }

    public function addPages( array $pages )
    {
      $this->admin_pages = $pages;

      return $this;
    }

    public function addAdminMenu()
    {
      foreach ( $this->admin_pages as $page ) {
        add_menu_page( $page['page_title'], $page['menu_title'], $page['capability'], $page['menu_slug'], $page['callback'], $page['icon_url'], $page['position'] );
      }
    }
  }

.. important::
  In the above class, method addPages() returns `$this`, which enables a call chain: you can call other methods of this class immediately after calling addPages(). such as in the class Admin.php::

    public function register() 
    {
      $this->settings->addPages( $this->pages )->register();
    }

  where **$this->settings** is a instance of class SettingsApi.