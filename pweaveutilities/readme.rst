Pweave Utilities (Read Me)
==========================


This code is meant to augment my use of `pweave <https://pypi.python.org/pypi/Pweave>`_, which has changed the way that I write python programs in a substantial way, putting me in the position of writing python code in a non-standard way. Python programmers who pull my code will likely say to themselves "What's with all these 'pnw' and 'rst' files?" (well, I've only heard it once, but I haven't written anything that's been widely shared). This code is meant to make it easier to separate out python, `pnw`, and `rst` files so that I can keep working in the same way but sort things out if I need to. In writing this I've also discovered that there's more to *pweave* than I originally knew about so this will also serve to document what I've found in the hopes that I'll get better at using it.

The updating code is hosted on `github <https://github.com/rsnakamura/pweaveutilities>`_.

The Finder
----------

To start with I grabbed an implementation of `find` that I've had for a while (taken from `David Beazley <http://www.dabeaz.com/generators/>`_) so that I could find relevant files. I took it so that the other code could use it, but since it was there I decided to make a command-line-interface for it::

   finder -h


.. code::

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
    
    


