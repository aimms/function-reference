.. aimms:procedure:: DataFileGetGroup(datafile, group)

.. _DataFileGetGroup:

DataFileGetGroup
================

With the procedure :aimms:func:`DataFileGetGroup` you can obtain the group name
associated with the user that currently owns a specific case or dataset.

.. code-block:: aimms

    DataFileGetGroup(
            datafile,      ! (input) element in the set AllDataFiles
            group          ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``.

    *group*
        A scalar string valued parameter. On return this parameter will contain
        the group name associated with the user that owns the datafile. If there
        is no current owner, or if the project does not have a user database
        associated with it, then an empty string is returned.

Return Value
------------

    The procedure returns 1 if the given datafile exists, and 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetOwner`.
