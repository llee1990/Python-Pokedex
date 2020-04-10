"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
from pokeretriever import PokedexObject
from PokeAPI import PokedexAPI
import asyncio


class PokedexObjectCreator(ABC):

    def __init__(self, queries):
        self.poke_api = PokedexAPI()
        self.queries = queries

    @abstractmethod
    def create_pokedex_object(self):
        """
        Creates Pokedex object
        :return my_pokedex_object:
        """
        pass


"""
Factory Class makes PokemonCreator object
"""


class PokemonCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Pokemon objects
        :return my_pokemon: as a Pokemon object
        """

        for request in self.queries:
            yield PokedexObject.Pokemon(**request)

    def parse_extra_data(self, pokemon):
        
        stats = pokemon.stats
        moves = pokemon.moves
        abilities = pokemon.abilities
        poke_moves = []
        poke_stats = []
        poke_abilities = []
        for stat in stats:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            stats_query = loop.run_until_complete(
                self.poke_api.process_requests("stat", stat))
            if len(stats_query) == 1:
                poke_stats.append(stats_query)
            else:
                poke_stats = stats_query
        for move in moves:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            move_query = loop.run_until_complete(
                self.poke_api.process_requests("move", move))
            if len(move_query) == 1:
                poke_moves.append(move_query)
            else:
                poke_moves = move_query
        for ability in abilities:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            ability_query = loop.run_until_complete(
                self.poke_api.process_requests("ability", ability))
            if len(ability_query) == 1:
                poke_abilities.append(ability_query)
            else:
                poke_abilities = ability_query
        self.__insert_data_in_pokemon(pokemon, poke_moves, poke_stats,
                                      poke_abilities)

    @staticmethod
    def __insert_data_in_pokemon(pokemon, moves, stats, abilities):
        pokemon.moves.clear()
        pokemon.stats.clear()
        pokemon.abilities.clear()
        for move in MoveCreator(moves).create_pokedex_object():
            pokemon.moves.append(move)
        for stat in StatsCreator(stats).create_pokedex_object():
            pokemon.stats.append(stat)
        for ability in AbilityCreator(abilities).create_pokedex_object():
            pokemon.abilities.append(ability)

"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        for request in self.queries:
            yield PokedexObject.Move(**request)


"""
Factory class for making Stats objects
"""


class StatsCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Stats object
        :return mystat: as a Stats object
        """
        for request in self.queries:
            yield PokedexObject.Stats(**request)


"""
Factory class for making Ability object
"""


class AbilityCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Ability objects
        :return:
        """
        for request in self.queries:
            yield PokedexObject.Ability(**request)