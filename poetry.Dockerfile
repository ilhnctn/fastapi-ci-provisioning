ARG IMAGE=python:3.10-slim
FROM $IMAGE

ENV USER=appuser
ENV HOME=/home/$USER
ENV APPDIR=$HOME/code

RUN mkdir -p $APPDIR

WORKDIR $APPDIR

# Install Poetry
RUN pip3 install poetry

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry install

COPY mbapp/ mbapp

EXPOSE 8081

CMD ["poetry", "run", "uvicorn", "myapp.app.app:app", "--host", "0.0.0.0", "--port", $APP_PORT]
