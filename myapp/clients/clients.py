from abc import ABC
from abc import abstractmethod
from logging import getLogger
from typing import Dict

import httpx
import requests

CLIENT_TIMEOUTS = (1, 5)

logger = getLogger(__name__)


class BaseDataClient(ABC):
    def __init__(self, config: Dict = None):
        if config:
            for k, v in config.items():
                setattr(self, k, v)

    @abstractmethod
    def get_data(self, *args, **kwargs) -> Dict:
        """Gets data from given resource.

        :param args: Named arguments.
        :param kwargs: Keyword arguments
        :return: Dict[Any]
        """
        pass


class AbstractWebClient(BaseDataClient):
    def get_data(self, url: str) -> Dict:
        """Fetches data from given url.

        :param url:
        :return:
        """
        pass


class ReqresDataClient(AbstractWebClient):
    def get_data(self, url: str) -> Dict:
        """

        :param url:
        :return:
        """
        try:
            response = requests.get(url=url, timeout=CLIENT_TIMEOUTS)
        except Exception as e:
            logger.error("Not good")
            raise Exception(message="Something bad happened. Details: " % e)
        return response.json()


class ReqresAsyncDataClient(BaseDataClient):
    """Async data client for Reqres API. For details, see https://reqres.in"""

    async def get_data(self, url: str = "https://reqres.in/api/users") -> Dict:
        async with httpx.AsyncClient(timeout=10, base_url=url) as client:
            result = await client.get(url=url)
            return result.json()


class AbstractDBClint(BaseDataClient):
    def __init__(self, config):
        self.config = config

    def get_data(self, *args, **kwargs) -> Dict:
        """Data client for database interactions.

        :param args:
        :param kwargs:
        :return:
        """
        pass

    @property
    def connection(self):
        pass


class AbstractPostgresClient(AbstractDBClint):
    pass
