FROM python:3.8

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# copy project
COPY . /app
VOLUME /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]