ARG IMAGE=python:3.10-slim
FROM $IMAGE

ENV USER=appuser
ENV HOME=/home/$USER
ENV APPDIR=$HOME/code

RUN mkdir -p $APPDIR

WORKDIR $APPDIR

COPY requirements/ requirements
RUN pip3 install --no-cache-dir --upgrade -r requirements/requirements.txt

COPY myapp/ myapp

EXPOSE 8080

CMD ["uvicorn", "myapp.app.app:app", "--host", "0.0.0.0", "--port", "8080"]
