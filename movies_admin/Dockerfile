FROM python:3.11
WORKDIR /opt/app
COPY . .
RUN pip install --upgrade pip && pip install poetry
RUN poetry export --without-hashes -f requirements.txt --output ./requirements.txt
RUN pip install -r ./requirements.txt

ENTRYPOINT python manage.py migrate && uwsgi --module=config.wsgi --http 0.0.0.0:8000
