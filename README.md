# mongodb-vs-postgres
mongobd-postgres benchmark

### Getting started

Project requires `python 3.10`, `docker` and `poetry` for getting started.

Prepare your local setup:
```bash
poetry install
```

For dockerized setup - it will run postgreSQL and mongoDB:
```bash
docker-compose up -d
```

Entering local virtualenv:
```bash
poetry shell
```

Inicialize both databases :
```bash
./manage migrate
./manage fill_db
./manage fill_db_pg
```

Run local server:
```bash
poetry runserver
```

URLs:
```bash
http://127.0.0.1:8000/pg/
http://127.0.0.1:8000/mongo/
```

Postgres results in [s]:
```bash
    "count": 500001,
    "time_count": 0.01942975216996274,
    "time_single_title": 0.0006074088400055188,
    "time_single_tag": 0.07671717789999093,
    "time_insert": 0.20403179557004478,
    "time_delete": 0.0001906621499801986,
    "time_relation": 0.0017063817100279265
```
MongoDB results in [s]:
```bash
    "count": 500001,
    "time_count": 0.2655898918299499,
    "time_single_title": 0.0013180223399831448,
    "time_single_tag": 1.493407641779995,
    "time_insert": 0.08796704377004062,
    "time_delete": 0.0974198059993796,
    "time_relation": 0.001126062089970219
```
