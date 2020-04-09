"""
Class PokedexObjectCreator
"""


class PokedexObjectCreator(ABC):
    def create_pokedex_object(self):
        """
        Creates Pokedex object
        :return my_pokedex_object:
        """
        my_pokedex_object = PokedexObject()
        return my_pokedex_object


"""
Factory Class makes PokemonCreator object
"""


class PokemonCreator(PokedexObjectCreator):
    def create_pokemon_object(self):
        """
        Creates Pokemon objects
        :return my_pokemon: as a Pokemon object
        """
        my_pokemon = Pokemon()
        return my_pokemon


"""
Factory Class makes Move objects 
"""


class MoveCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
         Creates Move objects
        :return my_move: as a Move object
        """
        my_move = Move()
        return my_move


"""
Factory class for making Stats objects
"""


class StatsCreator(PokedexObjectCreator):
    def create_pokedex_object(self):
        """
        Creates Stats object
        :return mystat: as a Stats object
        """
        my_stats = Stats()
        return my_stats


"""
Factory class for making Ability object
"""


class AbilityCreator():
    def create_pokedex_object(self):
        """
        Creates Ability objects
        :return:
        """
        my_ability = Ability()
        return my_ability