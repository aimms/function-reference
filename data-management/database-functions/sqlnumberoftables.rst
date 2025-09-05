.. aimms:function:: SQLNumberOfTables(Datasource, owner)

.. _SQLNumberOfTables:

SQLNumberOfTables
=================

With the function :aimms:func:`SQLNumberOfTables` you can determine the number of
tables in a datasource.

.. code-block:: aimms

    SQLNumberOfTables(
         Datasource,          ! (input) a string expression
         Owner                ! (input/optional) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *owner*
        A string containing the owner for which the number of tables must be
        determined. If the datasource doesn't support the owner concept, but the
        owner argument is specified, an error will be raised.

Return Value
------------

    The function returns the number of tables in the specified datasource.
    If there are no tables for the specified datasource and owner, 0 is
    returned. If an error occurs when determining the number of tables, ``-1``
    is returned and an error message is displayed in the error window.

.. seealso::

    - The functions :aimms:func:`SQLNumberOfViews`, :aimms:func:`SQLNumberOfColumns` and :aimms:func:`SQLTableName`.
