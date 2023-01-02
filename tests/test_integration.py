import pytest

api_url = "https://reqres.in/api/users"


@pytest.mark.asyncio
async def test_api_is_reachable_async(async_client):
    response = await async_client.get_data(url=api_url)

    assert "page" in response.keys()
    assert "total" in response.keys()


def test_api_is_accessible(sync_client):
    response = sync_client.get_data(url=api_url)
    assert "page" in response.keys()
    assert "total" in response.keys()
