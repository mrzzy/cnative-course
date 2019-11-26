#
# Memento
# Backend
# Dockefile
#

# TODO: specify base image with FROM

RUN mkdir /backend 
RUN mkdir /scripts 
# TODO: make /backend the home and current working directory

# install packages & pip modules
RUN apk add --no-cache postgresql-libs bash && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev 

# TODO: install pip modules

RUN apk --purge del .build-deps
ENV PATH=/backend/.local/bin:$PATH

# copy container scripts
COPY containers/backend /scripts
RUN chmod u+x -R /scripts

# TODO: add scripts to path

# TODO: copy application source code
# copy project source code

# TODO: expose the backend server port

# TODO: container entrypoint: run the application
