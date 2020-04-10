"""
Parses the command line arguments and formats data from a request
to Pokemon API
"""
import argparse
import enum
from pokeretriever import PokedexObjectCreator
from pokeretriever.PokeAPI import PokedexAPI
import asyncio


class ModeEnum(enum.Enum):

    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request:
    """
    The request object represents a request. The request object comes
     with certain accompanying configuration options as well as a field
     that holds the result. The attributes are:
        - mode: This is the mode data positional argument.
        - expanded: This is a flag
        - input_data:
        - input_file: The text file that contains the string.
        This is None if the data is not coming from a file.
        - output_file:help() This is the output method that is
        requested.
        The program supports printing to console or
         writing to another text file.
    """

    def __init__(self, mode: str, expanded: bool, input_data=None,
                 input_file=None, output_file=None):
        """
        Initializes Request object with the following attributes
        :param mode: as a str
        :param expanded:as a bool
        :param input_data:as a None or str
        :param input_file:as a None or str
        :param output_file:as a None or str
        """
        if input_file is not None and not input_file.endswith(".txt"):
            raise Exception
        self.poke_api = PokedexAPI()
        for pokedex_mode in ModeEnum:
            if mode == pokedex_mode.value:
                self.mode = pokedex_mode
        self.input_data = [input_data]
        self.expanded = expanded
        self.input_file = input_file
        self.output_file = output_file
        if self.input_file is not None:
            self.__convert_file_to_data()

    def __convert_file_to_data(self):
        with open(file=self.input_file, mode='r', encoding='UTF-8') as file:
            self.input_data = [line.rstrip('\n').lower() for line in file]

    def parse_request(self) -> dict or [dict]:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        query = loop.run_until_complete(
            self.poke_api.process_requests(self.mode.value, self.input_data))
        return query

    def __str__(self):
        """
        Returns a string of Request attributes
        :return:
        """
        return f"Mode: {self.mode}\n"\
               f"Input data: {self.input_data}\n"\
               f"Input file: {self.input_file}\n"\
               f"Expanded: {self.expanded}\n"\
               f"Output file: {self.output_file}\n"


class Pokedex:

    pokedex_object_factory_mapper = {
        ModeEnum.POKEMON: PokedexObjectCreator.PokemonCreator,
        ModeEnum.ABILITY: PokedexObjectCreator.AbilityCreator,
        ModeEnum.MOVE: PokedexObjectCreator.MoveCreator
    }

    def __init__(self, request: Request):
        self.request = request
        self.creator = self.pokedex_object_factory_mapper[self.request.mode]
        self.pokedex_object_container = []

    def populate_pokedex(self):
        data = self.request.parse_request()
        creator = self.creator(data)
        for pokedex_object in creator.create_pokedex_object():
            self.pokedex_object_container.append(pokedex_object)

    def print_contents(self):
        if self.request.output_file is None:
            for pokedex_object in self.pokedex_object_container:
                print(pokedex_object)
        else:
            with open(file=self.request.output_file, mode='w',
                      encoding='UTF-8') as file:
                for pokedex_object in self.pokedex_object_container:
                    file.write(str(pokedex_object) + '\n')


def setup_commandline_request():
    """
    Implements argparse module accepting arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If argpause fails
    then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str,
                        choices=["pokemon", "ability", "move"],
                        help="Either one of pokemon, ability, "
                             "or move must be chosen. The pokedex will query "
                             "information based on the chosen mode.")
    file_or_data = parser.add_mutually_exclusive_group(required=True)
    file_or_data.add_argument("--inputfile", type=str,
                              help="If providing a filename, "
                                   "filename must end with a .txt  extension.")
    file_or_data.add_argument("--inputdata", type=str,
                              help="If proving an id, id must be a "
                                   "digit. If providing a name, name must "
                                   "be a string.")
    parser.add_argument("--expanded", action="store_true",
                        help="Will the Pokedex be in expanded mode? "
                             "Only pokemon queries support the expanded "
                             "mode.\nDefault: False")
    parser.add_argument("--output", type=str,
                        help="The output filename, must end with "
                             "a .txt extension. If this flag is not provided, "
                             "print the result to the console.")
    args = parser.parse_args()
    return args


def main():

    cmd_args = setup_commandline_request()
    print(cmd_args)
    new_request = Request(mode=cmd_args.mode,
                          input_file=cmd_args.inputfile,
                          input_data=cmd_args.inputdata,
                          expanded=cmd_args.expanded,
                          output_file=cmd_args.output)
    # new_request = Request(mode="move",
    #                       input_file="request.txt",
    #                       input_data=None,
    #                       expanded=False,
    #                       output_file="output.txt")
    pokedex = Pokedex(new_request)
    pokedex.populate_pokedex()
    pokedex.print_contents()


if __name__ == '__main__':
    main()
