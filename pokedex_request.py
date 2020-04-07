"""
Module makes a request to pokemon API and returns data in a json
format for Activity mode and outputs data in a readable form.
"""

import asyncio
import aiohttp
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


class PokedexObject(ABC):

    def __init__(self, name: str, id_: int) -> None:
        self.name = name
        self.id = id_

""" Class Pokemon """


class Pokemon(PokedexObject):

    def __init__(self, name, id_):
        """
       Initializes attributes of Pokemon class
       """
        super().__init__(name, id_)
        # self.ab_data = None
        # self.name = None
        # self.id = None
        self.height = None
        self.weight = None
        self.stats = None
        self.types = None
        self.abilities = None
        self.moves = None

    def translate_data(self, api_dict):
        """ Transfers api data into pokemon
        object attributes
        """
        self.ab_data = api_dict
        self.name = self.ab_data['name']
        self.id = self.ab_data['id']
        self.height = self.ab_data['height']
        self.weight = self.ab_data['weight']
        self.stats = self.ab_data['stats']
        self.types = self.ab_data['types']
        self.abilities = self.ab_data['abilities']
        self.moves = self.ab_data['moves']

        # for item in self.ab_data['pokemon']:
        #     self.pokemons.append(element['pokemon']['name'])

    def __str__(self):
        """
        Prints out pokemon attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id}\nHeight:{self.height} decimeters" \
            f"\nWeight:{self.weight} hectograms\nStats:{self.stats} \nTypes:{self.types}"\
            f"\nAbilities:{self.abilities}\n Move: {self.moves}\n"


class Move(PokedexObject):

    def __init__(self, name: str, id_: int, generation: str, accuracy: int,
                 pp: int, power: int, move_type: str, dmg_class: str,
                 effect_short: str):
        super().__init__(name, id_)
        # self.name = name
        # self.id = id
        self.generation = generation
        self.accuracy = accuracy
        self.effect_short = effect_short
        self.pp = pp
        self.power = power
        self.move_type = move_type
        self.dmg_class = dmg_class

    def __str__(self):
        return f"Move name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.move_type}\n" \
               f"Damage class: {self.dmg_class}\n" \
               f"Effect(short): {self.effect_short}\n"


class Ability(PokedexObject):
    """
    Ability class for creating Ability objects from pokemon API
    """

    def __init__(self, name: str, id_: int, generation: str,
                 effect: str, effect_short: str, pokemon: [str]):
        """
        Initializes ability object with the following attributes
        :param name:as a str
        :param id_:as a int
        :param generation: as a str
        :param effect:as a str
        :param effect_short:as str
        :param pokemon: as a list of str
        """
        super().__init__(name, id_)
        # self.name = name
        # self.id = id_
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        """
        Returns string of Ability attributes
        :return str:
        """
        return f"Ability name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(short): {self.effect_short}\n" \
               f"pokemon: {self.pokemon}\n" \



class Stats(PokedexObject):
    def __init__(self, name, id_):
        """
       Initializes attributes of Stats class
       """
        super().__init__(name, id_)
        self.ab_data = None
        # self.name = None
        # self.id = None
        self.isBattleOnly = None

    def translate_data(self, api_dict):
        """
        Translates api data into stats data
        """
        self.ab_data = api_dict
        self.name = self.ab_data['name']
        self.id = self.ab_data['id']
        self.isBattleOnly = self.ab_data['is Battle Only']

    def __str__(self):
        """
        Prints out stats' attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id}\nIs Battle Only:" \
            f"{self.isBattleOnly}\n"


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
