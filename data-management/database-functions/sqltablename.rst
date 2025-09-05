.. aimms:function:: SQLTableName(Datasource, TableNo, Owner)

.. _SQLTableName:

SQLTableName
============

With the function :aimms:func:`SQLTableName` you can determine the name of a
certain table in a datasource. This function is designed to be used in
conjunction with the ``SQLNumberOfTables`` function.

.. code-block:: aimms

    SQLTableName(
         Datasource,          ! (input) a string expression
         TableNo,             ! (input) an integer expression
         Owner                ! (input/optional) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *TableNo*
        An integer containing the number of the table for which you want to
        retrieve the name. To determine the maximum value of this argument,
        please use the function ``SQLNumberOfTables`` prior to calling this
        function. The minimum value of this argument is 1.

    *Owner*
        A string containing the owner of the table for which the name must be
        determined. If the datasource doesn't support the owner concept, but the
        owner argument is specified, an error will be raised.

Return Value
------------

    The function returns the name of the table, with the number as specified
    through the ``TableNo`` argument.

.. note::

    Typically, this function can best be used in a construction like the
    following: 

    .. code-block:: aimms

            NumberOfTables := SQLNumberOfTables("MyDataSource");

            while LoopCount <= NumberOfTables do
                TableName := SQLTableName("MyDataSource", LoopCount);
                ! Do something with the retrieved table name here...
            endwhile;

.. seealso::

    - The functions :aimms:func:`SQLNumberOfTables` and :aimms:func:`SQLViewName`.
