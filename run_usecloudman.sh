#!/bin/bash
set -e
LOGFILE=/home/eafgan/ucm.org/access.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2
# User/group to run as
USER=eafgan
GROUP=users
# This assumes we cloned the source into the following dir
cd /home/eafgan/ucm.org/usecloudman/
# Activate the virtual env
source ../bin/activate
# Start the web app as a gunicorn-managed wsgi app
exec ../bin/gunicorn usecloudman.wsgi:application \
  -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE \
  -b localhost:8001
