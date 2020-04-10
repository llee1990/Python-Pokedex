"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
from pokeretriever import PokedexObject
from PokeAPI import PokedexAPI
import asyncio


class PokedexObjectCreator(ABC):

    def __init__(self, queries, expanded=None):
        self.poke_api = PokedexAPI()
        self.queries = queries
        self.expanded = expanded

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
            pokemon = PokedexObject.Pokemon(**request)
            if self.expanded:
                self.__expanded_mode(pokemon)
            else:
                self.__unexpanded_mode(pokemon)
            yield pokemon

    @staticmethod
    def __unexpanded_mode(pokemon):
        pokemon.stats = [stat['stat']['name'] + ": " +
                         str(stat['base_stat'])
                         for stat in pokemon.stats]
        pokemon.moves = [move['move']['name'] + ": lvl " +
                         str(move['version_group_details'][0][
                                 'level_learned_at'])
                         for move in pokemon.moves]
        pokemon.abilities = [ability['ability']['name']
                             for ability in pokemon.abilities]


    def __expanded_mode(self, pokemon):
        
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
                self.poke_api.process_requests(
                    "stat", stat['stat']['name']))
            poke_stats.append(stats_query)
        for move in moves:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            move_query = loop.run_until_complete(
                self.poke_api.process_requests(
                    "move", move['move']['name']))
            poke_moves.append(move_query)
        for ability in abilities:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            ability_query = loop.run_until_complete(
                self.poke_api.process_requests(
                    "ability", ability['ability']['name']))
            poke_abilities.append(ability_query)
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