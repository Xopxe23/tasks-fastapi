#!/bin/bash

alembic upgrade +1
alembic upgrade +1

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:80