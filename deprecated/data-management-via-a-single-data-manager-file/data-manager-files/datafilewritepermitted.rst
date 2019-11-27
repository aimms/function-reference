.. aimms:procedure:: DataFileWritePermitted(datafile)

.. _DataFileWritePermitted:

DataFileWritePermitted
======================

With the procedure :aimms:func:`DataFileWritePermitted` you can check whether the
current user has write permission for the specified case or dataset. For
example, you can use this procedure to issue your own error message if
the permission is not granted. If the current user does not have write
permission, then any call to a data manager procedure that involves a
write (save) operation will result in an error message, and fails.

.. code-block:: aimms

    DataFileWritePermitted(
            datafile      ! (input) element in the set AllDataFiles
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``.

Return Value
------------

    The procedure returns 1 if the current user does have write permission,
    and 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedure :aimms:func:`DataFileReadPermitted`.
