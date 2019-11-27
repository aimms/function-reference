.. aimms:procedure:: TestDatabaseColumn(Datasource, TableName, ColumnName)

.. _TestDatabaseColumn:

TestDatabaseColumn
==================

With the procedure :aimms:func:`TestDatabaseColumn` you can check whether a given
column is present in a database table on a specific datasource.

.. code-block:: aimms

    TestDatabaseColumn(
         Datasource,         ! (input) a string expression
         TableName           ! (input) a string expression
         ColumnName          ! (input) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *TableName*
        A string containing the name of a table in *Datasource*.

    *ColumnName*
        A string containing the name of a column in the *TableName*.

Return Value
------------

    The procedure returns 1 if the column name is present in the given
    database table, or 0 otherwise. If the result is 0, the pre-defined
    identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. note::

    The *TableName* and *ColumnName* arguments of the procedure
    :aimms:func:`TestDatabaseColumn` are case sensitive if the ODBC driver is case
    sensitive.

.. seealso::

    The procedures :aimms:func:`TestDataSource` and :aimms:func:`TestDatabaseTable`.
