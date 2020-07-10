.. _gulp:

Original: `Gulp getting started <http://zetcode.com/gulp/getting-started/>`_

Gulp Quick Start
==================
**Gulp** is a Node command-line task runner. Gulp let us automate processes and run repetitive tasks with ease. It is a streaming build system in front-end web development. It helps automate such tasks as copying files, linting, unit testing, image manipulation, minifying JavaScript and CSS code, or compiling TypeScript to JavaScript. Gulp is platform independent. In addition to Node.js, Gulp is used in .NET, Java, or PHP platforms.

Gulp favours code over configuration. It uses tasks to define its workflow. The tasks are written in the gulpfile.js file. Gulp tasks use plugins, which are small, single-purpose code units. The Gulp ecosystem includes more than 3500 such plugins. For instance, the gulp-minify plugin minifies JS files.

Gulp is based on Node streams. It reads data from a filesystem and passes them through pipelines to transform them. The data goes from one plugin to another with the use of the pipe function. One task is performed at a time. Using plugins in the pipeline allows to perform complex tasks. The original data may be modified, or we can create new modified copy of the data.

The gulp.src function creates the stream of source files to perform the pipe operations on. The gulp.dest specifies where to output the files once the task is completed.

Gulp CLI
-------------
Gulp consists of two parts: the Gulp library and the Gulp CLI (Command Line Interface). The Gulp library is used in JavaScript code. The gulp-cli is a utility program that allows us to access Gulp from the shell. In order to work with Gulp, we need to install both packages.

Gulp task
-------------
A Gulp task is an asynchronous JavaScript function. The function returns a stream, promise, event emitter, child process, or observable. Originally the tasks were created with the gulp.task function. Gulp now favours newer syntax based on modules, while the older syntax is still supported.

The modern syntax allows to separate the tasks into private and public. Public tasks are exported from the gulpfile, which allows them to be run by the gulp command. Private tasks are used only internally; we cannot run them with the gulp command.

Globbing
------------
Globbing is locating files on a file system using one or more glob strings. A glob string is a literal and/or wildcard characters, like *, **, or !, used to match filepaths.

::

  *.js

This glob matches all JS files.

::

  **/*.js: 

This glob string matches any file ending with .js in the root folder and any child directories.

::

  !main.scss: 

The ! indicates that the main.scss should be excluded.

::

  *.+(scss|sass)

This glob string matches any file that ends either in scss or sass.

Composing tasks
----------------
Gulp.js 4.0 introduces the series and parallel methods to combine tasks. The series runs tasks one by one, while the parallel runs tasks simultaneously::

  gulp.series(gulp.parallel(a, b), gulp.series(c, d))

In this case, first the a and b tasks are run in parallel, then, once both are complete, the c task is run and after it finishes, the d is run.

Gulp default task
-------------------
The default task is run when we do not provide any task name to the Gulp CLI tool::

  gulp.task('default', function() {
    ...
  });

  # The above is the older syntax to define a default task.

.. code-block:: 

  exports.default = function() {
    ...
  }

  # This is the newer syntax.

Prerequisites
--------------
Gulp is a command-line tool, so you should be familiar with working in the terminal. In order to use Gulp, you need to have Node.js installed on your system.

**Install Gulp**

To use Gulp, you need to install it as a global module first through NPM::

  sudo npm install --global gulp-cli

Start a Nodejs Gulp project
-----------------------------
In the project directory, run the command::

  npm init
  npm install --save-dev gulp
  # "--save-dev" option will save the installed tools' info into the composer.json file.

This will initiate a node project and install gulp files in the local folder. You will find a package.json file in the folder:

.. code-block:: json
  :linenos:

  {
    "name": "gulp-tutorial",
    "version": "1.0.0",
    "description": "This is an awesome tutorial.",
    "main": "index.js",
    "scripts": {
      "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [
      "node",
      "gulp",
      "js",
      "scss"
    ],
    "author": "Robert Zhou",
    "license": "GPL-3.0",
    "devDependencies": {
      "gulp": "^4.0.2"
    }
  }

.. important:: In a gulp project, each module including gulp itself must use command::

    npm install --save-dev node-gulp-module
  
  to install so that module information is stored in the json file.

.. important:: When working on an existing project, you should be carefull about the compaibility between node version and gulp version. e.g. gulp version < 4.0 is not compatible with node version > 12.0. You should switch to a proper node version before intiating command `npm install`.

  Please refer to :ref:`Manage Node Version <nodejs>` for how to switch node versions.

Gulp composing tasks example
-----------------------------
In this example, we compose tasks with series and parallel. In this example, we need gulp-minify, gulp-rename, gulp-clean-css, and del plugins.

The gulp-clean-css minifies CSS. The del deletes files and directories.

Install modules required::

  npm i --save-dev gulp-minify
  npm i --save-dev gulp-rename
  npm i --save-dev gulp-clean-css
  npm i --save-dev del

::

  src/
  ├── js
  │   └── main.js
  └── styles
      └── main.css
  We have this directory structure.

.. code-block:: 

  # src/js/main.js

  function hello() {

      return 'Hello there!';
  }

  hello();
  
  #This is a simple main.js file.

.. code-block:: 
 
  # src/styles/main.css

  body {
    font-family:georgia; font-size:1em;
    line-height:1.7em;
    background: #333;
    text-align:center;
  }
  
  # This is a simple main.css file.

We compile the `gulpfile.js` to include required tasks.

::

  #file: gulpfile.js

  const { src, dest, series, parallel } = require('gulp');
  const minify = require("gulp-minify");
  const rename = require("gulp-rename");
  const cleanCSS = require('gulp-clean-css');
  const del = require('del');


  const clean = () => del([ 'dist' ]);

  function styles() {

      return src('src/styles/main.css', { allowEmpty: true }) 
          .pipe(cleanCSS())
          .pipe(rename({
            basename: 'main',
            suffix: '.min'
          }))
          .pipe(dest('dist/styles'))
  }

  function scripts() {

      return src('src/js/main.js', { allowEmpty: true }) 
          .pipe(minify({noSource: true}))
          .pipe(dest('dist/js'))
  }

  const build = series(clean, parallel(styles, scripts));

  exports.styles = styles;
  exports.scripts = scripts;
  exports.clean = clean;
  exports.build = build;

  exports.default = build;

The gulpfile minifies CSS and JS files. It cleans the distribution directory. The workflow is separated into several tasks.

::

  const clean = () => del([ 'dist' ]);

The clean task removes the dist directory.

::

  function styles() {

      return src('src/styles/main.css', { allowEmpty: true }) 
          .pipe(cleanCSS())
          .pipe(rename({
            basename: 'main',
            suffix: '.min'
          }))
          .pipe(dest('dist/styles'))
  }

The styles task minifies the CSS file and renames it. It adds the .min extension.

::

  function scripts() {

      return src('src/js/main.js', { allowEmpty: true }) 
          .pipe(minify({noSource: true}))
          .pipe(dest('dist/js'))
  }

The scripts task minifies the JS file.

::

  const build = series(clean, parallel(styles, scripts));

We define a build task. It is a composition of three tasks. First, the clean task is run. After it finishes, the styles and scripts are run in parallel.

::

  exports.styles = styles;
  exports.scripts = scripts;
  exports.clean = clean;
  exports.build = build;

  exports.default = build;

We export five functions. The tasks can be called independently or composed in the build taks. Also, the build task is the default task.

::

  $ gulp build
  [15:17:01] Using gulpfile ~/gulp-lib/gulpfile.js
  [15:17:01] Starting 'build'...
  [15:17:01] Starting 'clean'...
  [15:17:01] Finished 'clean' after 13 ms
  [15:17:01] Starting 'styles'...
  [15:17:01] Starting 'scripts'...
  [15:17:01] Finished 'scripts' after 53 ms
  [15:17:01] Finished 'styles' after 54 ms
  [15:17:01] Finished 'build' after 70 ms

We explicitly run the build task.