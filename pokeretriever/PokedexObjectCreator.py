"""
Class PokedexObjectCreator
"""

from abc import ABC, abstractmethod
import PokedexObject


class PokedexObjectCreator(ABC):

    def __init__(self, request):
        self.request = request

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
        return PokedexObject.Pokemon(**self.request)


"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        return PokedexObject.Move(**self.request)


"""
Factory class for making Stats objects
"""


class StatsCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Stats object
        :return mystat: as a Stats object
        """
        return PokedexObject.Stats(**self.request)


"""
Factory class for making Ability object
"""


class AbilityCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Ability objects
        :return:
        """
        return PokedexObject.Ability(**self.request)