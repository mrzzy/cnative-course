#
# Cnative Course
# Containers - Frontend
# Dockerfile
# 

# TODO: specify base image with FROM

RUN mkdir /frontend 
RUN mkdir /scripts 
# TODO: make /frontend the home and current working directory

# install package depden
COPY src/frontend/package.json /frontend/
COPY src/frontend/yarn.lock /frontend/
# TODO: install dependent packages

# copy scripts
COPY containers/frontend /scripts
RUN chmod -R u+x /scripts/

# TODO: add scripts to path

# TODO: copy application source code

# TODO: expose the frontend server port

# TODO: container entrypoint: run the application
