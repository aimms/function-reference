.. aimms:procedure:: TestDatabaseTable(Datasource, Tablename)

.. _TestDatabaseTable:

TestDatabaseTable
=================

With the procedure :aimms:func:`TestDatabaseTable` you can check whether a given
table name exists in a specific data source.

.. code-block:: aimms

    TestDatabaseTable(
         Datasource,         ! (input) a string expression
         Tablename           ! (input) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *Tablename*
        A string containing the name of a table in *Datasource*.

Return Value
------------

    The procedure returns 1 if the database table is present in the given
    data source, or 0 otherwise. If the result is 0, the pre-defined
    identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. note::

    The *Tablename* argument of the procedure :aimms:func:`TestDatabaseTable` is case
    sensitive if the ODBC driver is case sensitive.

.. seealso::

    The procedures :aimms:func:`TestDataSource` and :aimms:func:`TestDatabaseColumn`.
