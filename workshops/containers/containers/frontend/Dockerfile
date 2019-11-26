#
# Cnative Course
# Containers - Frontend
# Dockerfile
# 

# TODO: specify base image with FROM
FROM node:12.2.0-alpine

RUN mkdir /frontend 
RUN mkdir /scripts 
# TODO: make /frontend the home and current working directory
ENV HOME=/frontend/
WORKDIR /frontend

# install package depden
COPY src/frontend/package.json /frontend/
COPY src/frontend/yarn.lock /frontend/
# TODO: install dependent packages
RUN yarn install

# copy scripts
COPY containers/frontend /scripts
RUN chmod -R u+x /scripts/

# TODO: add scripts to path
ENV PATH=/scripts:$PATH

# TODO: copy application source code
COPY src/frontend /frontend

# TODO: expose the frontend server port
EXPOSE 3000

# TODO: container entrypoint: run the application
ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD [ "yarn", "start" ]
