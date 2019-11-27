.. aimms:procedure:: LoadDatabaseStructure(Datasource)

.. _LoadDatabaseStructure:

LoadDatabaseStructure
=====================

The AIMMS ``Read ...From Table ...`` and ``Write ...To Table ...`` statements
offer a very flexible way to connect to data tables stored in an ODBC
compliant database. The AIMMS execution engine queries the structure of
the corresponding database tables in order to check whether the
connection between the table in the database and the AIMMS identifiers
can be set up in a valid way, and, if so, how to handle the statements
efficiently. Retrieving structural information may cost a significant
amount of time, depending on the number of tables, the quality of the
network and the quality of the ODBC database driver implementation in
providing this information. Although AIMMS already buffers this
information for each table after first use, retrieving this information
anew each AIMMS run might still be prohibitively expensive in some
cases. Therefore, AIMMS offers intrinsic database functions to empower
the app developer with caching this information outside AIMMS. With the
procedure :aimms:func:`LoadDatabaseStructure` you can load the cached database
table structure information.

.. code-block:: aimms

    LoadDatabaseStructure(
         Filename          ! (input) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of the file containing the database table
        structure information.

Return Value
------------

    The procedure returns 1 if the database table structure information is
    successfully loaded, or 0 otherwise.

.. seealso::

    The procedure :aimms:func:`SaveDatabaseStructure`
