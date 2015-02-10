The Finder
==========

.. code:: python

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




This adds a command-line interface to the :ref:`find generator <find-generator>`.

The Command Line Interface
--------------------------

This will create the command line arguments.

.. _finder-arguments:

Arguments Class
~~~~~~~~~~~~~~~

This is a class to (hopefully) make spelling errors easier to catch. The attributes are the names of the options and arguments in the `docopt` dictionary.


.. code:: python

    class Arguments(object):
        """
        Constants to reduce typing errors
        """
        __slots__ = ()
        expression = "<expression>"
        root = "--root"
        shallow = "--shallow"
        regex = "--regex"
    



Glob From None
~~~~~~~~~~~~~~

This is a function to convert the ``expression`` argument to a default based on whether the expectation is to match a glob or a regular expression (or not to set anything if the user passed in an *expression*). If the user didn't specify anything then the expression will be set to match everything. It wouldn't really make sense for someone to specify a regular expression and then not set the expression but I figured I had to handle the case where they did anyway.

.. image:: figures/finder_glob_from_none.svg

.. module:: pweaveutilities.finder
.. autosummary::
   :toctree: api

   glob_from_none




This might seem like overkill, but it was originally meant to be used by the schema to validate the glob before I decided to allow a default regular expression as well as a default glob.

The Schema
~~~~~~~~~~

This is the *schema* to validate arguments given by the user.

.. csv-table:: Arguments Schema
   :header: Argument, Schema, Default

   ``<expression>``, :math:`String \lor None`, None
   ``--root``, :math:`Path \lor None`, None
   ``--shallow``, :math:`True \lor False`, False
   ``--regex``, :math:`True \lor False`, False

.. highlight:: python


.. code:: python

    finder_schema_dict = {Arguments.expression: Or(None, str),
                        Arguments.root: Or(None, os.path.exists),
                        Arguments.shallow: Use(bool),
                        Arguments.regex: Use(bool)}
    schema = Schema(finder_schema_dict)



Setup Finder
------------

This sets up the finder. It was originally part of the `main` function but I want to use it in other parts of the code too.

.. autosummary::
   :toctree: api

   setup_finder





The Main
--------

.. autosummary::
   :toctree: api

   main

The Main Procedure.

   #. get and validate the command-line arguments
   #. set finder to deep or shallow find based on arguments
   #. set default matching expression if not given
   #. generate the names


.. code:: python

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


