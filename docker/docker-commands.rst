.. _dockerCommands:

Docker Commands
=================

`docker ps` and `docker container ls`
-------------------------------------
Command `"docker ps"` or `"docker container ls"` will list active containers' info::

  $ docker ps
  CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS              PORTS                                      NAMES
  1e1a72ca6d42        nginx:latest                   "nginx -g 'daemon of…"   3 days ago          Up 3 days           80/tcp                                     wp3-nginx
  e7cea7a2aacf        alphacodinghub/wordpress-fpm   "/entrypoint.sh php-…"   3 days ago          Up 3 days           9000/tcp                                   wp3-fpm
  21a1dc2424c5        mariadb:10.5                   "docker-entrypoint.s…"   3 days ago          Up 3 days           3306/tcp                                   wp3-db
  1119bb9319c4        redis:5-alpine                 "docker-entrypoint.s…"   3 days ago          Up 3 days           6379/tcp                                   wp3-redis
  a22e8b2d1b87        nginx:latest                   "nginx -g 'daemon of…"   10 days ago         Up 10 days          80/tcp                                     wp2-nginx
  ccccf5914026        alphacodinghub/wordpress-fpm   "/entrypoint.sh php-…"   10 days ago         Up 10 days          9000/tcp                                   wp2-fpm

To show container ID only, you can use command `"docker ps -aq"` or `"docker container ls -aq"`::

  $ docker ps -aq
  1e1a72ca6d42
  e7cea7a2aacf
  21a1dc2424c5
  1119bb9319c4
  a22e8b2d1b87

This is very useful when you want to stop or remove all active containers::

  $ docker stop `docker ps -aq`
  1e1a72ca6d42
  e7cea7a2aacf
  21a1dc2424c5
  1119bb9319c4
  a22e8b2d1b87
  
  $ docker ps -a
  CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS                        PORTS               NAMES
  1e1a72ca6d42        nginx:latest                   "nginx -g 'daemon of…"   3 days ago          Exited (0) 46 seconds ago                         wp3-nginx
  e7cea7a2aacf        alphacodinghub/wordpress-fpm   "/entrypoint.sh php-…"   3 days ago          Exited (0) 46 seconds ago                         wp3-fpm
  21a1dc2424c5        mariadb:10.5                   "docker-entrypoint.s…"   3 days ago          Exited (0) 45 seconds ago                         wp3-db
  1119bb9319c4        redis:5-alpine                 "docker-entrypoint.s…"   3 days ago          Exited (0) 46 seconds ago                         wp3-redis
  a22e8b2d1b87        nginx:latest                   "nginx -g 'daemon of…"   10 days ago         Exited (0) 46 seconds ago                         wp2-nginx

We can see all containers stopped running.

We can remove containers using command::

  $ docker container rm `docker ps -aq`

Or, start all stopped containers::

  $ docker container start `docker ps -aq`

Or, re-start all containers::

  $ docker container restart `docker ps -aq`

  