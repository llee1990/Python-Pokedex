"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
import PokedexObject


class PokedexObjectCreator(ABC):

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
    def create_pokemon_object(self):
        """
        Creates Pokemon objects
        :return my_pokemon: as a Pokemon object
        """
        pokemon = PokedexObject.Pokemon()
        return pokemon


"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        move = PokedexObject.Move()
        return move


"""
Factory class for making Stats objects
"""


class StatsCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Stats object
        :return mystat: as a Stats object
        """
        stats = PokedexObject.Stats()
        return stats


"""
Factory class for making Ability object
"""


class AbilityCreator():
    def create_pokedex_object(self):
        """
        Creates Ability objects
        :return:
        """
        ability = PokedexObject.Ability()
        return ability