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

# copy application source code
COPY src/frontend /frontend

# development build entrypoint
EXPOSE 3000
CMD yarn start

## production build
# build production files
RUN yarn build

# copy production files to new production stage
FROM node:12.2.0-alpine AS production
RUN mkdir -p /serve
COPY --from=develop /frontend/build /serve

# install production server
RUN yarn init --yes && yarn add serve

# production entrypoint
EXPOSE 3000
CMD yarn serve -l 3000 -s /serve
