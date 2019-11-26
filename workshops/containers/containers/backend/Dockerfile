#
# Memento
# Backend
# Dockefile
#

# TODO: specify base image with FROM
FROM python:3.7-alpine 

RUN mkdir /backend 
RUN mkdir /scripts 
# TODO: make /backend the home and current working directory
ENV HOME=/backend/
WORKDIR /backend

# install packages & pip modules
RUN apk add --no-cache postgresql-libs bash && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \

    
# TODO: install pip modules
COPY src/backend/requirements.txt /backend/
RUN python3 -m pip install -r requirements.txt --no-cache-dir

RUN apk --purge del .build-deps
ENV PATH=/backend/.local/bin:$PATH

# copy container scripts
COPY containers/backend /scripts
RUN chmod u+x -R /scripts

# TODO: add scripts to path
ENV PATH=/scripts:$PATH

# TODO: copy application source code
# copy project source code
COPY src/backend /backend/

# TODO: expose the backend server port
EXPOSE 5000

# TODO: container entrypoint: run the application
ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD python run.py
