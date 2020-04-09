import argparse
import enum

"""
Parses the command line arguments and formats data from a request
to Pokemon API
"""


class ModeEnum(enum.Enum):

    POKEMON = 0
    ABILITY = 1
    MOVES = 2


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
        self.mode = mode
        self.input_data = input_data
        self.expanded = expanded
        self.input_file = input_file
        self.output_file = output_file

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
                             "or move must "
                             "be chosen. The pokedex will query "
                             "information based on the chosen mode.")
    file_or_data = parser.add_mutually_exclusive_group(required=True)
    file_or_data.add_argument("--inputfile", type=str,
                              help="If providing a filename, "
                                   "filename must "
                                   "end with a .txt extension.")
    file_or_data.add_argument("--inputdata", type=str,
                              help="If proving an id, id must be a "
                                   "digit. If "
                              "providing a name, name must be a string.")
    parser.add_argument("--expanded", action="store_true",
                        help="Will the Pokedex be in expanded mode? "
                             "Only "
                             "pokemon queries support the "
                             "expanded mode.\n"
                             "Default: False")
    parser.add_argument("--output", type=str,
                        help="The output filename, must end with "
                             "a .txt "
                             "extension. If this flag is not provided, "
                             "print the result to the console.")
    args = parser.parse_args()
    return args


def main():
    """
    Runs Program
    :return:
    """
    cmd_args = setup_commandline_request()
    print(cmd_args)
    new_request = Request(cmd_args.mode, cmd_args.expanded,
                          cmd_args.inputdata, cmd_args.inputfile,
                          cmd_args.output)
    print(new_request)


if __name__ == '__main__':
    main()
