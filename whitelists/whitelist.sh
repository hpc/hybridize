#!/bin/sh
#
# chkconfig: 345 25 75
# description: find bootup files
#
# This file should have start permissions immediately following nfsd.  It
# assumes /.timestamp has been touched by a script that runs first in the
# boot sequence, e.g. /etc/rc.d/rc.sysinit (or whatever the System
# initialization program is set to in /etc/inittab).

case "$1" in
   start) 
   echo "Starting whitelist: "

   find / \
      -path /dev -prune -o \
      -path /panfs -prune -o \
      -path /proc -prune -o \
      -path /sys -prune -o \
      -path /users -prune -o \
      -path /var/lib/perceus -prune -o \
      -anewer /.timestamp \
      -not -lname /var/lib/perceus\* \
      -print > /tmp/whitelist
esac
