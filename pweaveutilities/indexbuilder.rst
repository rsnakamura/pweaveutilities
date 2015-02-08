Index Builder
=============




.. module:: pweaveutilities.indexbuilder

.. _index-builder-introduction:
Introduction
------------

To try and ease the building of the Table of Contents for folders once the modules start exploding (which they inevitably do) they will be auto-generated. To do so the following two assumptions will be made:

    #. Any file with the extension `.rst` that is not `index.rst` should be included in the `index.rst` in the same folder

    #. Any folder in the same directory that has an `index.rst` file should include the sub-folder `index.rst`

    #. The first non-empty line of each included file should be used as the displayed name in the table of contents

.. note:: This means that if any sub-folder does not have an `index.rst` file then its sub-folders will not be included.

The Headline Grabber
--------------------

Since the convention for creating tables of contents is to use the form::

    pretty name <filename>

The first non-empty line of the included files will be used as the `pretty name`.

.. autosummary::
   :toctree: api

    grab_headline




Subfolder Toctree
-----------------

For sub-folders there are different cases. I think most of the time it is easiest just to grab them all up, but often it is more meaningful to add commentary to the indices which will require that they be grabbed individually (here is where use-cases might be helpful).

.. autosummary::
   :toctree: api

   subfolder_toctree





The Toctree Creator
-------------------

.. autosummary::
   :toctree: api

   create_toctree




This function will generate a toctree by applying the :ref:`assumptions <index-builder-introduction>` mentioned above. To be safe it will add an empty line above and below the output. For this to work the weaving code will need to turn off echoing (and wrapping) and using 'sphinx' for the results.

Here's an example call::

    create_toctree(maxdepth=1)

.. '    



.. toctree::
   :maxdepth: 1

   Generators <generators.rst>
   Index Builder <indexbuilder.rst>

.. toctree::
   :maxdepth: 1

   Testing the Utilities <tests/index.rst>







