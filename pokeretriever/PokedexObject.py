"""
"""

from abc import ABC


class PokedexObject(ABC):
    """
    Base Class of Pokemon classes
    """
    def __init__(self, name: str, id: int, **kwargs) -> None:
        """
        Initializes attributes of PokedexObject class
        :param name: as type str
        :param id: as type int
        """
        self.name = name
        self.id = id


class Move(PokedexObject):
    """
    Move class makes Move objects
    """

    def __init__(self, generation: [str], accuracy: int,
                 pp: int, power: int, type: {str}, damage_class: {dict},
                 effect_entries: [dict], **kwargs):
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
        self.generation = generation['name']
        self.accuracy = accuracy
        self.effect_short = effect_entries[0]['short_effect']
        self.pp = pp
        self.power = power
        self.type = type['name']
        self.damage_class = damage_class['name']

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
               f"Type: {self.type}\n" \
               f"Damage class: {self.damage_class}\n" \
               f"Effect(short): {self.effect_short}\n"


class Ability(PokedexObject):
    """
    Ability class for creating Ability objects from pokemon API
    """

    def __init__(self, generation: dict, effect_entries: [dict], pokemon: [dict], **kwargs):
        """
        Initializes ability object with the following attributes

        :param generation: as a str
        :param effect:as a str
        :param effect_short:as str
        :param pokemon: as a list of str
        """
        super().__init__(**kwargs)
        self.generation = generation['name']
        self.effect = effect_entries[0]['effect']
        self.effect_short = effect_entries[0]['short_effect']
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
    def __init__(self, is_battle_only, **kwargs):
        """
       Initializes attributes of Stats class
       """
        super().__init__(**kwargs)
        self.isBattleOnly = is_battle_only

    def __str__(self):
        """
        Prints out stats' attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id}\nIs Battle Only:" \
            f"{self.isBattleOnly}\n"


class Pokemon(PokedexObject):
    """
    Pokemon child class creates Pokemon object
    """

    def __init__(self, height: int, weight: int, stats: [dict],
                 types: [dict], abilities: [dict], moves: [dict], **kwargs):
        """
       Initializes attributes of Pokemon class
       """
        super().__init__(**kwargs)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        """
        Prints out pokemon attributes and their values
        """
        return f"\nName:{self.name}\nId: {self.id}\nHeight:{self.height}" \
            f"\nWeight:{self.weight}\nStats:{self.stats} \n" \
            f"Types:{self.types}\nAbilities:{self.abilities}\n" \
            f"Move: {self.moves}\n"
