.. _gulpSass:

Gulp Sass tutorial
======================
Gulp Sass tutorial shows how to compile Sass to CSS with gulp-sass plugin.

From: `Gulp Sass tutorial <http://zetcode.com/gulp/sass/>`_

Gulp
-----
Gulp is a Node task runner. It is a streaming build system in front-end web development. It helps automate such tasks as copying files, minifying JavaScript code, or compiling TypeScript or CoffeeScript to JavaScript.

Sass
-------
Sass is a preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS). Sass has two syntaxes; the older syntax uses indentation to separate code blocks and newline characters to separate rules.

The newer syntax, SCSS, uses block formatting like CSS. It uses braces to denote code blocks and semicolons to separate lines within a block. The indented syntax and SCSS files are traditionally given the extensions .sass and .scss, respectively.

The gulp-sass plugin
----------------------
The gulp-sass is a Gulp plugin for compiling Sass to CSS. Internally it uses the node-sass module.

Installing Gulp and gulp-sass
-------------------------------
We initiate a Node.js project and install Gulp and gulp-sass plugin.

:: 
  $ npm init -y 
  $ npm i --global gulp-cli
  $ npm i gulp --save-dev
  # We initiate a Node project and install Gulp and Gulp CLI.

::

  $ npm i --save-dev gulp-sass
  $ npm i --save-dev del
  # We install the gulp-sass plugin and the del module, which deletes files using Promise API and has support for multiple files and globbing.

Gulp-sass example
-----------------------
The following example demonstrates the usage of gulp-sass module.

::

  $ mkdir sass
  $ mkdir css
  $ touch index.html gulpfile.js sass/main.scss

We create two directories and three empty files::

  .
  │   gulpfile.js
  │   index.html
  │   node_modules
  │   package-lock.json
  │   package.json
  │
  ├───css
  └───sass
          main.scss

This is the project structure. The index.html file uses CSS for its layout. The CSS is generated into the css directory. The SCSS is located inside the main.scss file in the sass directory.

index.html:

.. code-block:: html
  :linenos:

  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link rel="stylesheet" href="css/main.css">
      <title>Bugs</title>
  </head>
  <body>

  <div class="container">

      <h1>Bugs</h1>

      <table>

          <tr>
              <th>Bug name</th>
              <th>Description</th>
          </tr>

          <tr>
              <td>Assasin bug</td>
              <td>The assassin bug uses its short three-segmented beak to pierce
                  its prey and eat it.</td>
          </tr>

          <tr>
              <td>Bed bug</td>
              <td>Bed bugs are parasitic insects in the that feed exclusively
                  on blood.</td>
          </tr>

          <tr>
              <td>Carpet beetle</td>
              <td>Considered a pest of domestic houses and, particularly, natural
                  history museums where the larvae may damage natural fibers and
                  can damage carpets, furniture, clothing, and insect collections.</td>
          </tr>

          <tr>
              <td>Earwig</td>
              <td>Earwigs are mostly nocturnal and often hide in small, moist
                  crevices during the day, and are active at night, feeding on
                  a wide variety of insects and plants.</td>
          </tr>

      </table>

  </div>

  </body>
  </html>

This is the `index.html` file. The link tag includes CSS from `css/main.css` file.

File sass/main.scss:

.. code-block:: 
  :linenos:

  $myfont: Georgia 1.2em;
  $table_head_col: #ccc;
  $table_row_col: #eee;
  $table_bor_col: #eee;
  $container_width: 700px;
  $first_col_width: 150px;

  div.container {

      margin: auto; 
      font: $myfont;
      width: $container_width;
  }

  table {

      tr:nth-child(odd) {background: $table_row_col}

      td:first-child {width: $first_col_width}
    
      th {
          background-color: $table_head_col;
      }

      border: 1px solid $table_bor_col;
  }

This is the SCSS code to be compiled into CSS.

gulpfile.js::

  const gulp = require('gulp');
  const sass = require('gulp-sass');
  const del = require('del');

  gulp.task('styles', () => {
      return gulp.src('sass/**/*.scss')
          .pipe(sass().on('error', sass.logError))
          .pipe(gulp.dest('./css/'));
  });

  gulp.task('clean', () => {
      return del([
          'css/main.css',
      ]);
  });

  gulp.task('default', gulp.series(['clean', 'styles']));

This is the gulpfile.js that contains our Gulp tasks::

  gulp.task('styles', () => {
      return gulp.src('sass/**/*.scss')
          .pipe(sass().on('error', sass.logError))
          .pipe(gulp.dest('./css/'));
  });

The gulp.task() creates a new task, which we call styles. The gulp.src() creates a stream for reading all SCSS files. With pipe() we pass the streamed data to the sass compiler. In the end, we pass the compiled data to the gulp.dest(), which in turn creates a stream for writing the data to the file system.

::

  gulp.task('clean', () => {
      return del([
          'css/main.css',
      ]);
  });

The clean task deletes the generated CSS file.

::

  gulp.task('default', gulp.series(['clean', 'styles']));

The default task is a task that is executed if no task name is specified with Gulp CLI. It runs the clean and styles tasks in sequential order.

::

  $ gulp
  [13:07:10] Using gulpfile ~\Documents\js\gulpsass\gulpfile.js
  [13:07:10] Starting 'default'...
  [13:07:10] Starting 'clean'...
  [13:07:10] Finished 'clean' after 4.11 ms
  [13:07:10] Starting 'styles'...
  [13:07:11] Finished 'styles' after 14 ms
  [13:07:11] Finished 'default' after 23 ms

We run the default task. The CSS file is generated.

Gulp watch task
-----------------
We can use gulp.watch() to automatically watch for changes.

::

  gulp.task('watch', () => {
      gulp.watch('sass/**/*.scss', (done) => {
          gulp.series(['clean', 'styles'])(done);
      });
  });

Note that watching for files may take a lot of resources; therefore, we should be careful with gulp.watch().

In this tutorial we have used Gulp to compile SCSS code into CSS.
