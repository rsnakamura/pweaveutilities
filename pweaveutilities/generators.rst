Generators
==========



A module to hold the generators for the concatenator.




The regex match filter
----------------------

To support both regular expressions and globs I'll create an alternative filter.

.. '

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




The Shallow Find Class
----------------------

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

This doesn't travel down into a path-tree. It just searches the top-level

.. '   




The `concantenate` Generator
----------------------------

.. autosummary::
   :toctree: api

   concatenate
             


