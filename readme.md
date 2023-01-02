# Outline
The goal of this repo is to demonstrate an end to end flow for a web application.

## Modules
All the app related modules are listed under [mbapp](myapp) directory.

|Module Name|Path|Description|
|---|---|---|
|assets|[assets](myapp/assets)|Web UI template & assets.|
|app|[app](myapp/app)|Contains web app related components.|
|clients|[clients](myapp/clients)|Contains client classes for external data access.|

## Local Development
You can use [poetry](https://python-poetry.org/docs/) for packaging and deployment purposes.


### Environment Variables
Required environment variables can be seen from [dev.env.sample](./envs/dev.env.sample) file.
Variables are also set under CI variables in the repository ([link](https://gitlab.com/ilhnctn/mb-case/-/settings/ci_cd))

```shell script
poetry install
export DATA_API_URL=...
export SENTRY_DSN=...

poetry run uvicorn app.app:app --reload --host 0.0.0.0 --port 8080
...

poetry run pytest -x -vv 
```

TODO: Due to an issue in [poetry.Dockerfile(./poetry.Dockerfile)], currently `pip install -r requirements.txt` must be used in containers.

**Docker**

```shell script
export IMAGE_TAG=server-template:v1 
docker build -t $IMAGE_TAG .

docker run -p 8080:8080 $IMAGE_TAG

```
API docs can be seen from `http://127.0.01:8080/docs` in OpenAPI format.

## Test & Deployment Pipeline
The pipeline can be seen from [gitlab-ci](./.gitlab-ci.yml) file.

# TODOs
 - Add terraform & internet access.
 - Integrate Infra provisioning to the pipeline.
 - Scan image, container and package for security risks

## Nice To Have
 - Item per page filter in UI
 - UI tests
 