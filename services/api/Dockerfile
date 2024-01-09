FROM python:3.10-slim-buster

ENV WORKDIR=/usr/src/app
ENV USER=app
ENV APP_HOME=/home/app/web
ENV LOG_DIR=/home/app/logs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR $WORKDIR

RUN pip install --upgrade pip
COPY ./requirements.txt $WORKDIR/requirements.txt
RUN pip install -r requirements.txt

RUN adduser --system --group $USER
RUN mkdir $APP_HOME
RUN mkdir $LOG_DIR
WORKDIR $APP_HOME

COPY . $APP_HOME
RUN chown -R $USER:$USER $APP_HOME
RUN chown -R $USER:$USER $LOG_DIR
USER $USER
