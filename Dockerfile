FROM python:3.7.3

RUN apt update && apt upgrade -y && apt install -y postgresql-client

ENV BASE_DIR /app
VOLUME ["$BASE_DIR"]
WORKDIR $BASE_DIR

COPY requirements.txt $BASE_DIR/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . $BASE_DIR/
RUN DATABASE_URL=postgres://none REDIS_URL=none python manage.py collectstatic  --noinput

# make sure static files are writable by uWSGI process
RUN chown -R 1000:2000 $BASE_DIR/media

ENV DJANGO_SETTINGS_MODULE=eunabox.settings.production

EXPOSE 8000

CMD ["uwsgi" , "--ini=/app/conf/uwsgi.ini"]