# docker run -p 8000:8000 app
FROM python:3.10-bullseye

RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY main.py .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0