.. aimms:function:: CloseDataSource(Datasource)

.. _CloseDataSource:

CloseDataSource
===============

With the procedure :aimms:func:`CloseDataSource` you can temporarily close the
connection to a data source. AIMMS automatically opens the connection to
a data source if needed, and closes the connection when the project is
exited.

.. code-block:: aimms

    CloseDataSource(
         Datasource          ! (input) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

.. note::

    When :aimms:func:`CloseDataSource` is called during a transaction that was
    explicitly started by calling :aimms:procedure:`StartTransaction` the transaction is rolled back
    before actually closing the data source. :aimms:set:`CurrentErrorMessage` contains a message
    telling it did so.
