# Dockerfile

# pull the official docker image
FROM python:3.10.10-buster

# set work directory
WORKDIR /web

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["sh", "-c", "sleep 5 && flask db upgrade && gunicorn --bind 0.0.0.0:5000 app:app"]
# copy project
COPY . .
