"""
Module makes a request to pokemon API and returns data in a json
format for Activity mode and outputs data in a readable form.
"""

import asyncio
import aiohttp
from PokedexObjectCreator import PokedexObjectCreator
from abc import ABC


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
    async def get_pokedex_data(url, session) -> dict:
        """
        Makes request to API and returns a json formatted data
        :param url: as string
        :param session: as string
        :return json_response as a dict:
        """
        response = await session.request(method="GET", url=url)
        json_response = await response.json()
        return json_response

    async def __process_single_request(self, request_type: str, req_id):
        """
        Processes single request for call to Pokemon site
        :param request_type: as a str
        :param req_id: as an int
        :return response: as a dict
        """
        url = self.url + f"{request_type}/{req_id}"
        async with self.session() as session:
            response = await self.get_pokedex_data(url, session)
            return response

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


class JSONtoObjectConverter:

    def __init__(self, api: PokedexAPI, creator: PokedexObjectCreator):
        self.api = api
        self.creator = creator

    def create_pokedexobject(self):
        responses = api.process_requests()







def main():
    """
    Runs program
    :return:
    """
    requests = [1, 2, 3]
    # requests = "stench"
    pokedex = PokedexAPI()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    moves = loop.run_until_complete(pokedex.process_requests(
        "move", requests))
    move_list = [Move(move['name'], move['id'],
                      move['generation']['name'],
                      move['accuracy'], move['pp'],
                      move['power'],
                      move['type']['name'],
                      move['damage_class']['name'],
                      move['effect_entries'][0]['short_effect'])
                 for move in moves]
    for move in move_list:
        print(move)

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    abilities = loop.run_until_complete(
        pokedex.process_requests("ability", requests))
    if isinstance(abilities, dict):
        ability = Ability(abilities['name'], abilities['id'],
                          abilities['generation']['name'],
                          abilities['effect_entries'][0]['effect'],
                          abilities[
                              'effect_entries'][0]['short_effect'],
                          abilities['pokemon'])
        print(ability)
    else:
        ability_list = [Ability(ability['name'], ability['id'],
                                ability['generation']['name'],
                                ability['effect_entries'][0]['effect'],
                                ability['effect_entries'][0]
                                ['short_effect'], ability[
                              'pokemon'])
                        for ability in abilities]
        for ability1 in ability_list:
            print(ability1)


if __name__ == "__main__":
    main()
