import os
from logging import getLogger

import sentry_sdk
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from myapp.clients import ReqresAsyncDataClient
from myapp.clients import ReqresDataClient

DATA_API_URL = os.environ.get("DATA_API_URL", "https://reqres.in/api/users")
SENTRY_DSN = os.environ.get("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
    )

app = FastAPI()
app.mount("/assets", StaticFiles(directory="mbapp/assets"), name="assets")

templates = Jinja2Templates(directory="mbapp/assets")


sync_client = ReqresDataClient()
async_client = ReqresAsyncDataClient()

logger = getLogger(__name__)


@app.get("/")
async def json_render(page: int = 1, per_page: int = 2):
    """Display data table from sync client.
    """
    response = await async_client.get_data(
        url=f"{DATA_API_URL}?page={page}&per_page={per_page}"
    )

    return response


@app.get("/html", response_class=HTMLResponse)
async def html_render(request: Request, page: int = 1, per_page: int = 2):
    """Display data table from Async data client. Default behaviour.

    :param request: Mandatory context manager.
    :param page:
    :param per_page:
    :return:
    """
    response = await async_client.get_data(
        url=f"{DATA_API_URL}?page={page}&per_page={per_page}"
    )
    return templates.TemplateResponse(
        "users.html", {"response": response, "request": request}
    )
