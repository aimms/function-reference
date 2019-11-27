.. aimms:procedure:: ListingFileCopy(toFileName, overwrite)

.. _ListingFileCopy:

ListingFileCopy
===============

With the procedure :aimms:func:`ListingFileCopy` you can copy the current contents
of the listing file to a given file.

.. code-block:: aimms

    ListingFileCopy(
         toFileName,         ! (input) string expression
         overwrite           ! (optional) default 1.
         )

Arguments
---------

    *toFileName*
        The file name of the file to which the contents of the listing file must
        be copied.

    *overwrite*
        if equal to 0 then do not overwrite an existing file, otherwise
        overwrite an existing file when needed.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The procedure :aimms:func:`ListingFileDelete`.
