The Mover
=========

.. code:: python

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




The `Mover` traverses file-paths and moves files matching a pattern to another directory with a different root name but the same folder structure under the other root.

Move
----

Since this is function-based, rather than class-based (for now) it seemed to make more sense to use verbs rather than nouns for the names.

.. module:: pweaveutilities.mover
.. autosummary::
   :toctree: api

   move




The Arguments
-------------

Most of the arguments take the same form as the :ref:`finder arguments <finder-arguments>` but the `root` is now an argument and there's an additional `<target>`.

.. '


.. code:: python

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
    



And now the schema is setup using the finder-schema as a starting point.


.. code:: python

    mover_schema_dict = finder_schema_dict
    del(mover_schema_dict[FinderArguments.root])
    mover_schema_dict[MoverArguments.root] = os.path.exists
    mover_schema_dict[MoverArguments.target] = str
    mover_schema = schema.Schema(mover_schema_dict)
    



Main
----

This provides an entry point for the command-line interface.

.. autosummary::
   :toctree: api

   main




