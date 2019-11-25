#
# Cnative Course
# Containers - Frontend
# Dockerfile
#

FROM node:12.2.0-alpine AS develop

RUN mkdir /frontend 
RUN mkdir /scripts 
ENV HOME=/frontend/
WORKDIR /frontend

# install dependent packages
COPY src/frontend/package.json /frontend/
COPY src/frontend/yarn.lock /frontend/
RUN yarn install

# copy scripts
COPY containers/frontend /scripts
RUN chmod -R u+x /scripts/
ENV PATH=/scripts:$PATH

# copy application source code
COPY src/frontend /frontend

# development build entrypoint
EXPOSE 3000
ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD [ "yarn", "start" ]
