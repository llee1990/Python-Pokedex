"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
from pokeretriever import PokedexObject
from pokeretriever.PokeAPI import PokedexAPI
import asyncio


class PokedexObjectCreator(ABC):

    def __init__(self, expanded=None):
        self.poke_api = PokedexAPI()
        self.expanded = expanded

    @abstractmethod
    async def create_pokedex_object(self, query):
        """
        Creates Pokedex object
        :return my_pokedex_object:
        """



"""
Factory Class makes PokemonCreator object
"""


class PokemonCreator(PokedexObjectCreator):
    async def create_pokedex_object(self, query):
        """
        Creates Pokemon objects
        :return my_pokemon: as a Pokemon object
        """

        pokemon = PokedexObject.Pokemon(**query)
        if self.expanded:
            await self.__expanded_mode(pokemon)
        else:
            self.__unexpanded_mode(pokemon)
        return pokemon

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

    async def __expanded_mode(self, pokemon):
        stats = pokemon.stats
        moves = pokemon.moves
        abilities = pokemon.abilities
        poke_moves = []
        poke_stats = []
        poke_abilities = []
        for stat in stats:
            stats_query = await self.poke_api.process_requests(
                "stat", stat['stat']['name'])
            poke_stats.append(stats_query)
        for move in moves:
            move_query = await self.poke_api.process_requests(
                "move", move['move']['name'])
            poke_moves.append(move_query)
        for ability in abilities:
            ability_query = await self.poke_api.process_requests(
                "ability", ability['ability']['name'])
            poke_abilities.append(ability_query)
        print(poke_stats[1])
        # poke_moves = await asyncio.gather(*poke_moves)
        # poke_stats = await asyncio.gather(*poke_stats)
        # poke_abilities = await asyncio.gather(*poke_abilities)
        await self.__insert_data_in_pokemon(pokemon, poke_moves, poke_stats,
                                            poke_abilities)

    @staticmethod
    async def __insert_data_in_pokemon(pokemon, moves, stats, abilities):
        pokemon.moves.clear()
        pokemon.stats.clear()
        pokemon.abilities.clear()
        moves_coroutines = [MoveCreator().create_pokedex_object(move) for
                            move in moves]
        stats_coroutines = [StatsCreator().create_pokedex_object(stat) for
                            stat in stats]
        ability_coroutines = [AbilityCreator().create_pokedex_object(ability)
                              for ability in abilities]
        moves_responses = await asyncio.gather(*moves_coroutines)
        stats_responses = await asyncio.gather(*stats_coroutines)
        ability_responses = await asyncio.gather(*ability_coroutines)
        pokemon.moves.append(moves_responses)
        pokemon.stats.append(stats_responses)
        pokemon.abilities.append(ability_responses)

"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    async def create_pokedex_object(self, query):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        return PokedexObject.Move(**query)


"""
Factory class for making Stats objects
"""


class StatsCreator(PokedexObjectCreator):
    async def create_pokedex_object(self, query):
        """
        Creates Stats object
        :return mystat: as a Stats object
        """
        return PokedexObject.Stats(**query)


"""
Factory class for making Ability object
"""


class AbilityCreator(PokedexObjectCreator):
    async def create_pokedex_object(self, query):
        """
        Creates Ability objects
        :return:
        """
        return PokedexObject.Ability(**query)