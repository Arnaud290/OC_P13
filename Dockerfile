FROM python:3.8-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN chown www-data /app/oc-lettings-site-sqlite3
RUN pip install -r requirements.txt

# copy project
COPY . /app
VOLUME /app

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser --disabled-password user
RUN usermod -a -G www-data user
USER user

# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
