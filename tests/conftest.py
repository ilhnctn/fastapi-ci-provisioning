import pytest

from myapp.clients import ReqresAsyncDataClient
from myapp.clients import ReqresDataClient


@pytest.fixture(scope="function")
def sync_client():
    return ReqresDataClient()


@pytest.fixture(scope="function")
def async_client():
    return ReqresAsyncDataClient()
