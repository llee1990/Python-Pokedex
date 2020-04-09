"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
from pokeretriever import PokedexObject


class PokedexObjectCreator(ABC):

    def __init__(self, requests):
        self.requests = requests

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
        for request in self.requests:
            yield PokedexObject.Pokemon(**request)


"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        for request in self.requests:
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
        for request in self.requests:
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
        for request in self.requests:
            yield PokedexObject.Ability(**request)