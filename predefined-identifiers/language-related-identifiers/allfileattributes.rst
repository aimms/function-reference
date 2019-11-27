.. aimms:set:: AllFileAttributes

.. _AllFileAttributes:

AllFileAttributes
=================

The predefined set :aimms:set:`AllFileAttributes` contains the attributes which
can be used in the filtering of files.

.. code-block:: aimms

        Set AllFileAttributes {
            Index      :  IndexFileAttributes;
            Definition :  data { Hidden, ReadOnly, Executable };
        }

Definition
----------

    The predefined set :aimms:set:`AllFileAttributes` contains the attributes the
    intrinsic functions :aimms:procedure:`DirectoryGetFiles`, and :aimms:procedure:`DirectoryGetSubDirectories` use to filter their result.
    They are:

    -  ``Hidden``: the file or subdirectory is normally not visible when
       querying the folder in which it resides,

    -  ``ReadOnly``: the file or subdirecotry is read only,

    -  ``Executable``: the file is executable (this attribute is ignored for
       DirectoryGetSubdirectories).

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The functions :aimms:func:`DirectoryGetFiles`, and :aimms:func:`DirectoryGetSubDirectories`.
