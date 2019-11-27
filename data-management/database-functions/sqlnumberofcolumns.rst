.. aimms:function:: SQLNumberOfColumns(Datasource, TableName, Owner)

.. _SQLNumberOfColumns:

SQLNumberOfColumns
==================

With the function :aimms:func:`SQLNumberOfColumns` you can determine the number of
columns of a database table.

.. code-block:: aimms

    SQLNumberOfColumns(
         Datasource,          ! (input) a string expression
         TableName,           ! (input) a string expression
         Owner                ! (input/optional) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *TableName*
        A string containing the name of the database table for which the number
        of columns must be determined.

    *Owner*
        A string containing the owner of the database table for which the number
        of columns must be determined. If the datasource doesn't support the
        owner concept, but the owner argument is specified, an error will be
        raised.

Return Value
------------

    The function returns the number of columns in the specified database
    table. If the database table doesn't exist, an error is raised.

.. seealso::

    The functions :aimms:func:`SQLNumberOfViews`, :aimms:func:`SQLNumberOfTables` and :aimms:func:`SQLColumnData`.
