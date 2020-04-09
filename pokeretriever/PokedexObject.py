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
        self.id_ = id_


""" Class Pokemon """


class Pokemon(PokedexObject):
    """
    Pokemon child class creates Pokemon object
    """

    def __init__(self, height: int, weight: int, stats: list,
                 type_: list, abilities: list, moves: list, **kwargs):
        """
       Initializes attributes of Pokemon class
       """
        super().__init__(**kwargs)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.type_ = type_
        self.abilities = abilities
        self.moves = moves
    #
    # def translate_data(self, api_dict):
    #     """ Transfers api data into pokemon
    #     object attributes
    #     """
    #     self.ab_data = api_dict
    #     self.name = self.ab_data['name']
    #     self.id = self.ab_data['id']
    #     self.height = self.ab_data['height']
    #     self.weight = self.ab_data['weight']
    #     self.stats = self.ab_data['stats']
    #     self.types = self.ab_data['types']
    #     self.abilities = self.ab_data['abilities']
    #     self.moves = self.ab_data['moves']
    #
    #     # for item in self.ab_data['pokemon']:
    #     #     self.pokemons.append(element['pokemon']['name'])

    def __str__(self):
        """
        Prints out pokemon attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id_}\nHeight:{self.height}" \
            f"\nWeight:{self.weight}\nStats:{self.stats} \n" \
            f"Types:{self.type_}\nAbilities:{self.abilities}\n" \
            f"Move: {self.moves}\n"


class Move(PokedexObject):
    """
    Move class makes Move objects
    """

    def __init__(self, generation: str, accuracy: int,
                 pp: int, power: int, move_type: str, dmg_class: str,
                 effect_short: str, **kwargs):
        """
        Initializes Move object

        :param generation:
        :param accuracy:
        :param pp:
        :param power:
        :param move_type:
        :param dmg_class:
        :param effect_short:
        """
        super().__init__(**kwargs)
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
               f"ID: {self.id_}\n" \
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

    def __init__(self, generation: str, effect: str, effect_short: str,
                 pokemon: list, **kwargs):
        """
        Initializes ability object with the following attributes

        :param generation: as a str
        :param effect:as a str
        :param effect_short:as str
        :param pokemon: as a list of str
        """
        super().__init__(**kwargs)
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
               f"ID: {self.id_}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(short): {self.effect_short}\n" \
               f"pokemon: {self.pokemon}\n" \



class Stats(PokedexObject):
    """
    Stats class
    """
    def __init__(self, battle_only, **kwargs):
        """
       Initializes attributes of Stats class
       """
        super().__init__(**kwargs)
        self.isBattleOnly = battle_only

    def __str__(self):
        """
        Prints out stats' attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id_}\nIs Battle Only:" \
            f"{self.isBattleOnly}\n"
