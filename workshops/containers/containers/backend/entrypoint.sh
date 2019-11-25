#!/bin/sh
#
# Memento
# Backend
# Container Entrypoint
#

## setup database
# wait for datebase to become available
echo "waiting for database to become available..."
if wait-for $DATABASE_HOST -t 30
then 
    # perform database migrations
    flask db upgrade
    # run command 
    exec "$@"
fi
