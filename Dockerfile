FROM python:3.8-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# copy project
COPY . /app
VOLUME /app

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# add and run as non-root user
RUN adduser arnaud
USER arnaud

# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT