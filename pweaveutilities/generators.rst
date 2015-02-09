Generators
==========



A module to hold the generators for the concatenator.




The regex match filter
----------------------

To support both regular expressions and globs I'll create an alternative filter. This uses python's `re.match` to see if a particular path matches what the user gave as the expression.

.. module:: pweaveutilities.generators
.. autosummary::
   :toctree: api

   regex_filter




.. _find-generator:

The `find` Generator
--------------------
 

.. autosummary::
   :toctree: api

   find

This function generates files that match the expression given. The default is to use `fnmatch.filter` to match unix-style wildcards (globs). If the *regex* argument is set to True, then regular expressions are used instead.




The Shallow Find Class
----------------------

The default *find* traverses down into sub-directories to find all matches. In some cases this isn't what's wanted. The `ShallowFind` class is a stateful implementation of a finder that only looks at the top directory, rather than traversing down into the sub-trees.

.. autosummary::
   :toctree: api

   ShallowFind
   ShallowFind.path
   ShallowFind.filenames
   ShallowFind.matching_names
   ShallowFind.matching_count
   ShallowFind.reset
   ShallowFind.__iter__




The `shallow_find` Generator
----------------------------

.. autosummary::
   :toctree: api

   shallow_find

This doesn't travel down into a path-tree. It just searches the top-level, but is implemented as a generating-function so doesn't maintain stat as with the *ShallowFind* class.




The `concantenate` Generator
----------------------------

.. autosummary::
   :toctree: api

   concatenate

This takes all files matching a glob and outputs their lines one after another.
             


