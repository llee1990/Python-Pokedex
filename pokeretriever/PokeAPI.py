"""
Module makes a request to pokemon API and returns data in a json
format for Activity mode and outputs data in a readable form.
"""

import asyncio
import aiohttp
from aiohttp import ClientPayloadError, web


class PokedexAPI:
    """
    Class makes request call or calls to Pokemon site and returns json
    formatted data
    """
    def __init__(self):
        """ Initializes the following attributes """
        self.url = "https://pokeapi.co/api/v2/"
        self.session = aiohttp.ClientSession

    @staticmethod
    async def get_pokedex_data(url, session, status=None) -> dict:
        """
        Makes request to API and returns a json formatted data
        :param url: as string
        :param session: as string
        :return json_response as a dict:
        """
        # response = await session.request(method="GET", url=url)
        try:
            response = await session.request(method="GET", url=url)
            json_response = await response.json()
            return json_response
        except Exception as e:
            status = 500
            print(f"status={status}")

    async def __process_single_request(self, request_type: str, req_id):
        """
        Processes single request for call to Pokemon site
        :param request_type: as a str
        :param req_id: as an int
        :return response: as a dict
        """
        url = self.url + f"{request_type}/{req_id}"
        try:
            async with self.session() as session:
                response = await self.get_pokedex_data(url, session)
                return response
        except ClientPayloadError:
            print(" Not the right content being loaded")
        except aiohttp.InvalidURL:
            print("Improper URL")

    async def process_requests(
            self, request_type: str, request: list or str):
        """
        Processes single or multiple requests for calls to Pokemon
        API
        :param request_type: as a str
        :param request: as a list or str
        :return responses: as a dict
        """
        if not isinstance(request, list):
            response = await self.__process_single_request(request_type,
                                                           request)
            return response
        else:
            url = self.url + "{}/{}"
            async with self.session() as session:
                list_urls = [url.format(
                    request_type, req_id) for req_id in request]
                coroutines = [self.get_pokedex_data(new_url, session) for
                              new_url in list_urls]
                responses = await asyncio.gather(*coroutines)
                return responses
