# Cloud Native/Containers - Practical
Practical for Workshop on Containers with Docker

## Intro
In this practical, we will apply the container know how we learnt by:
- use Docker to containerize a backend of a web application.
- use Docker to containerize a frontend of a web application.
- use Docker Compose hook up the containers to allow them to work together.
    - use a pre-built docker image to provide a database to the backend.
- deploy the stack on a Google Cloud server.

## App Infomation
Infomation about the web application used in this practical:
- Database - provides data storage for the backend 

| Attribute | Description | Value |
| --- | --- | --- |
| Kind | Kind of SQL Database Server | PostgreSQL 12.0 |
| Port | Port that the server listens on | 5432 |
| Storage Path | Path where the database server stores the data | `/var/lib/postgresql/data` |

| Environment Variable | Description |
| --- | --- |
| `POSTGRES_USER` | Username of the user used to authenticate with the database |
| `POSTGRES_PASSWORD` | Password of the user used to authenticate with the database |

- Backend - backend of the web application, exposes a REST API that the frontend uses

| Attribute | Description | Value |
| --- | --- | --- |
| Platform | Programming language used to implement the backend | Python 3.7 |
| Libraries | Library/Module dependencies used to implement the backend | Listed in `requirements.txt ` |
| Port | Port that the backend server listens on | 5000 |

| Environment Variable | Description |
| --- | --- |
| `SQL_DATABASE` | Kind of SQL Database to use (`sqlite` or `postgresql`) |
| `DATABASE_HOST` | DNS name/IP address of the database server. |
| `POSTGRES_USER` | Username of the user used to authenticate with the database |
| `POSTGRES_PASSWORD` | Password of the user used to authenticate with the database |

- Frontend - frontend of the web appication, displays a simple interface to
                create and delete organisations

| Attribute | Description | Value |
| --- | --- | --- |
| Platform | Frontend is built on NodeJS and the ReactJS framework | NodeJS 12.2.0 |
| Libraries | Library/Module dependencies used to implement the frontend | Listed in `package.json ` |
| Port | Port that the frontend server listens on | 3000 |

| Environment Variable | Description |
| --- | --- |
| `REACT_APP_API_HOST` | DNS name/IP address of the backend server |
