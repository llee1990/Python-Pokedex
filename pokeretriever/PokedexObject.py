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
        self.name = name.title()
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
        return f"------------------\nMove name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage class: {self.damage_class}\n" \
               f"Effect(short): {self.effect_short}"


class Ability(PokedexObject):
    """
    Ability class for creating Ability objects from pokemon API
    """

    def __init__(self, generation: dict, effect_entries: [dict],
                 pokemon: [dict], **kwargs):
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
        self.pokemons = [monster['pokemon']['name'] for monster in pokemon]

    def __str__(self):
        """
        Returns string of Ability attributes formatted
        :return string: of type str
        """
        pokemons = ', '.join(pokemon for pokemon in self.pokemons)
        return f"------------------\nAbility name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect(short): {self.effect_short}\n" \
               f"Pokemon:\n{pokemons}" \



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
        return f"------------------\nName: {self.name}\nId: {self.id}\nIs " \
            f"Battle Only: {self.isBattleOnly}"


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
        self.types = [pokemon_type['type']['name'] for pokemon_type in types]
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        """
        Prints out pokemon attributes and their values
        """
        if any(isinstance(stat, Stats) for stat in self.stats):
            stats = '\n'.join(str(stat) for stat in self.stats)
            abilities = '\n'.join(str(ability) for ability in self.abilities)
            moves = '\n'.join(str(move) for move in self.moves)
        else:
            stats = ', '.join(stat for stat in self.stats)
            abilities = ', '.join(ability for ability in self.abilities)
            moves = ', '.join(move for move in self.moves)
        types = ', '.join(pokemon_type for pokemon_type in self.types)
        return f"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-" \
            f"\nName: {self.name}\nId: {self.id}\nHeight: {self.height}" \
            f"\nWeight: {self.weight}\nTypes:\n{types}\n\n" \
            f">>STATS<<\n{stats}\n\n>>ABILITIES<<\n{abilities}\n" \
            f"\n>>MOVES<<\n{moves}\n" \
            f"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"
