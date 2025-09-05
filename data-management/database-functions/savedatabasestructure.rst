.. aimms:procedure:: SaveDatabaseStructure(Filename)

.. _SaveDatabaseStructure:

SaveDatabaseStructure
=====================

With the procedure :aimms:func:`SaveDatabaseStructure` you can save the database
table structure information such that this information can be quickly 
retrieved in subsequent AIMMS sessions. This procedure only stores the structure 
information for tables that are currently connected. 
In order to connect to a database table, you should either run a read or write statement, 
or open the mapping wizard of that database tables. Please note that calling :aimms:func:`CloseDataSource` 
will close all these connections, so this should not be called before the call to :aimms:func:`SaveDatabaseStructure`.

.. code-block:: aimms

    SaveDatabaseStructure(
         Filename           ! (input) a string expression
         )

Arguments
---------

    *Filename*
        A string containing the name of a data source.

Return Value
------------

    The procedure returns 1 if the database table structure is succesfully
    saved to file ``Filename``, or 0 otherwise.

.. seealso::

    - The procedure :aimms:func:`LoadDatabaseStructure`.
