"""
"""

from abc import ABC


class PokedexObject(ABC):
    """
    Base Class of Pokemon classes
    """
    def __init__(self, name: str, id_: int) -> None:
        """
        Initializes attributes of PokedexObject class
        :param name: as type str
        :param id_: as type int
        """
        self.name = name
        self.id = id_


""" Class Pokemon """


class Pokemon(PokedexObject):
    """
    Pokemon child class creates Pokemon object
    """

    def __init__(self, name, id_):
        """
       Initializes attributes of Pokemon class
       """
        super().__init__(name, id_)
        self.ab_data = None
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
    """
    Move class makes Move objects
    """

    def __init__(self, name: str, id_: int, generation: str, accuracy: int,
                 pp: int, power: int, move_type: str, dmg_class: str,
                 effect_short: str):
        """
        Initializes Move object
        :param name:
        :param id_:
        :param generation:
        :param accuracy:
        :param pp:
        :param power:
        :param move_type:
        :param dmg_class:
        :param effect_short:
        """
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
        """
        Returns Move object in formatted string
        :return:
        """
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
        Returns string of Ability attributes formatted
        :return string: of type str
        """
        return f"Ability name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(short): {self.effect_short}\n" \
               f"pokemon: {self.pokemon}\n" \



class Stats(PokedexObject):
    """
    Stats class
    """
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
