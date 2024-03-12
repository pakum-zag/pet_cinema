FROM python:3.11
WORKDIR /opt/app
COPY . .
RUN pip install --upgrade pip && pip install poetry
RUN poetry export --without-hashes -f requirements.txt --output ./requirements.txt
RUN pip install -r ./requirements.txt

ENTRYPOINT python main.py
