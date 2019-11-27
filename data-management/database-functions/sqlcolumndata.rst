.. aimms:function:: SQLColumnData(Datasource, TableName, ColumnNumber, Owner, ColumnCharacteristic)

.. _SQLColumnData:

SQLColumnData
=============

With the function :aimms:func:`SQLColumnData` you can determine the
characteristics of a certain column of a database table.

.. code-block:: aimms

    SQLColumnData(
         Datasource,          ! (input) a string expression
         TableName,           ! (input) a string expression
         ColumnNumber,        ! (input) an integer expression
         Owner,               ! (input/optional) a string expression
         ColumnCharacteristic ! (input/optional) an element in set AllData-
                                  ColumnCharacteristics, with default
                                  value 'Name'
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *TableName*
        A string containing the name of the database table of the column for
        which to retrieve a characteristic.

    *ColumnNumber*
        An integer containing the number of the column for which to retrieve a
        characteristic. The maximum value of this argument can be obtained by
        calling the function ``SQLNumberOfColumns`` prior to calling this
        function. The minimum value of this argument is 1.

    *Owner*
        A string containing the owner of the database table. If the datasource
        doesn't support the owner concept, but the owner argument is specified,
        an error will be raised.

    *ColumnCharacteristic*
        An element in the set :aimms:set:`AllDataColumnCharacteristics`, which contains all possible
        characteristics to obtain for a column.

Return Value
------------

    The function returns the specified characteristic, as a string value.
    This means that also the numerical characteristics (``'Width'``,
    ``'NumberOfDecimals'`` and (possibly) ``'DefaultValue'``) are returned
    as string values. So, if you want to use these results in their numeric
    form, please use the function ``Val``.

.. note::

    Typically, this function will be used in a construction like the
    following, to ensure that the right ``ColumnNumber`` argument is passed:

    .. code-block:: aimms

            NumberOfColumns := SQLNumberOfColumns("MyDataSource", "MyTable");

            ColCount := 1;
            while ColCount <= NumberOfColumns do
                for IndexDataColumnCharacteristics do
                    Characteristic := SQLColumnData(MyDataSource, "MyTable", ColCount, "",
                                                          IndexDataColumnCharacteristics);
                    ! Do something with the characteristic
                endfor;
                ColCount += 1;
            endwhile;

.. seealso::

    The functions :aimms:func:`SQLNumberOfColumns` and :aimms:func:`Val`.
