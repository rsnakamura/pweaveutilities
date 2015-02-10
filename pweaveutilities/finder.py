
"""
The Finder.

This is a recursive file-finder that travels down a path tree looking for files that match a glob. It was meant to be used by other code, but I thought it might be useful.

Usage:             finder [--shallow] [--regex] [<expression>] [--root=<root>]

Arguments:    
    <expression>        Glob (or regex) to match files (e.g. "*.pnw"). Quotes are required to prevent shell-expansion.

Options:
    -s, --shallow      List only what's in the root (don't traverse down the tree).
    -r, --root=<root>  Root directory to start search (defaults to current working directory).
    --regex            Intrepret the expression as a regex instead of a glob
    -h, --help         Show this screen.
    -v, --version      Show version.
"""

# python standard library
import os
# third-party
from docopt import docopt
from schema import Schema, Or, Use

# this package
import pweaveutilities.generators
from pweaveutilities import VERSION

class Arguments(object):
    """
    Constants to reduce typing errors
    """
    __slots__ = ()
    expression = "<expression>"
    root = "--root"
    shallow = "--shallow"
    regex = "--regex"

def glob_from_none(expresion, regex=False):
    """
    sets an expression to match all files if not given

    :param:

     - `expression`: the <expression> passed in by the user
     - `regex`: Boolean set by --regex

    :return: expression if not None or '*' or '.*' depending on regex
    """
    if expresion is None:
        if not regex:
            return '*'
        return '.*'
    return expresion

finder_schema_dict = {Arguments.expression: Or(None, str),
                    Arguments.root: Or(None, os.path.exists),
                    Arguments.shallow: Use(bool),
                    Arguments.regex: Use(bool)}
schema = Schema(finder_schema_dict)

def setup_finder(arguments):
    """
    Chooses the find function and expression based on the arguments

    :param:

     - `arguments`: validated dictionary of arguments

    :return: <find function> <glob-expression>
    """
    # decide if it will be a shallow or deep find
    find = pweaveutilities.generators.find
    if arguments[Arguments.shallow]:
        find = pweaveutilities.generators.shallow_find

    # check if you need a default glob that matches all files
    expression = glob_from_none(arguments[Arguments.expression],
                                arguments[Arguments.regex])
    return find, expression

def main():
    """
    The main entry point for the command-line find
    """
    # get and validate the arguments
    arguments = docopt(__doc__, version=VERSION)
    arguments = schema.validate(arguments)

    find, expression = setup_finder(arguments)

    # generate the names
    for name in find(expression=expression,
                     start=arguments[Arguments.root],
                     regex=arguments[Arguments.regex]):
        print(name)
    return