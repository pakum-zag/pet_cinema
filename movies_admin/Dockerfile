FROM python:3.11-bullseye
WORKDIR /opt/app
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml pyproject.toml
RUN pip install --upgrade pip && pip install poetry
RUN poetry export --without-hashes -f requirements.txt --output ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .
