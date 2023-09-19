#!/bin/bash

celery -A src.tasks.celery:celery worker -l INFO