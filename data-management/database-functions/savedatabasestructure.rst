.. aimms:procedure:: SaveDatabaseStructure(Filename)

.. _SaveDatabaseStructure:

SaveDatabaseStructure
=====================

With the procedure :aimms:func:`SaveDatabaseStructure` you can save the database
table structure information such that this information is quickly
retrieved in subsequent AIMMS sessions. Please note that you should
first make sure that you have connected to all datasources involved.
Information for tables contained in non-connected datasources is not
stored. In order to connect to a datasource, you should either run a
read or write statement using one of its tables, or open the mapping
wizard of one of its database tables. 
Only the active tables information will be stored, 
so if you want to have the complete database structure to be saved then all tables have to be active.

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

    The procedure :aimms:func:`LoadDatabaseStructure`.
