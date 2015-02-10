
"""
The Mover.

This moves files matching a glob from one folder to a new folder, re-creating the sub-folders.

Usage:  mover <expression> <root> <target> [--shallow] [--regex]

Arguments:

   <expression>   Glob or regex to match files.
   <root>         Root of source folder
   <target>       Root of target folder

Options:

   -s, --shallow  Don't traverse the tree
   -r, --regex    Intrepret `expression` as a regular expression instead of a glob.
"""

# python standard library
from distutils.util import strtobool as to_bool
import os
import shutil

# third-party
import docopt
import schema

# this package
from pweaveutilities.generators import find
from pweaveutilities.finder import Arguments as FinderArguments
from pweaveutilities.finder import setup_finder, finder_schema_dict
from pweaveutilities import VERSION

def move(source_glob, source_path, target_path, find_function=find, regex=False):
    """
    Moves files matching the source-glob in the source_path to the target_path

    :param:

     - `source_glob`: glob or regex to match files
     - `source_path`: root directory to move files from
     - `target_path`: root directory to move files to
     - `find_function`: function to find files
     - `regex`: boolean to indicate what `source_glob` is
    """
    # the replace needs to have a trailing slash
    # or it will be lost
    if not target_path.endswith('/'):
        target_path += '/'
    try:
        os.makedirs(target_path)
    except OSError:
        pass
    for path in find_function(source_glob, source_path, regex):
        target = path.replace(source_path, target_path)
        try:
            os.renames(path, target)
        except OSError as error:
            print(error)
            print("Failed to move '{0}' to '{1}'".format(path, target))
    return

class MoverArguments(object):
    """
    Arguments for the mover
    """
    __slots__ = ()
    expression = FinderArguments.expression
    root = "<root>"
    shallow = FinderArguments.shallow
    regex = FinderArguments.regex
    target = "<target>"

mover_schema_dict = finder_schema_dict
del(mover_schema_dict[FinderArguments.root])
mover_schema_dict[MoverArguments.root] = os.path.exists
mover_schema_dict[MoverArguments.target] = str
mover_schema = schema.Schema(mover_schema_dict)

def main():
    """
    gets the command line arguments and passes them to `move`
    """
    MOVER_DEBUG = to_bool(os.environ.get("MOVER_DEBUG", 'no'))
    if MOVER_DEBUG:
        import pudb
        pudb.set_trace()
    arguments = docopt.docopt(__doc__, version=VERSION)
    arguments = mover_schema.validate(arguments)
    find_function, expression = setup_finder(arguments)
    move(expression,
            arguments[MoverArguments.root],
            arguments[MoverArguments.target],
            find_function,
            regex=arguments[MoverArguments.regex])
    return