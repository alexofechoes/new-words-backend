FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN pip install poetry

WORKDIR /code

ADD poetry.lock pyproject.toml /code/
RUN POETRY_VIRTUALENVS_CREATE=false poetry install && \
    python -m nltk.downloader punkt wordnet

ADD . /code/

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
