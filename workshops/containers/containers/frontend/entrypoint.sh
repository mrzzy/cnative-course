#!/bin/sh
#
# Cloud Native/Containers 
# Workshop - Frontend
# Container Entrypoint
#

# wait for backend api to become available
echo "waiting for backend to become available..."
if wait-for $BACKEND_HOST -t 30
then 
    # run command 
    exec "$@"
fi
