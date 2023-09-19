FROM python:latest

RUN mkdir /tasks

WORKDIR /tasks

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /tasks/docker/*.sh

CMD ["gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:80"]