.. aimms:set:: AllDataColumnCharacteristics

.. _AllDataColumnCharacteristics:

AllDataColumnCharacteristics
============================

The predefined set :aimms:set:`AllDataColumnCharacteristics` contains all
possible column properties, which can be queried using the function
:aimms:func:`SQLColumnData`.

.. code-block:: aimms

        Set AllDataColumnCharacteristics {
            Index      :  IndexDataColumnCharacteristics;
            Definition :  {
                data { Name, DataType, Width,
                       NumberOfDecimals, IsPrimaryKey,
                       Nullable, DefaultValue, Remark }
            }
        }

Definition
----------

    The set :aimms:set:`AllDataColumnCharacteristics` contains all possible column
    properties, which can be queried using the function :aimms:func:`SQLColumnData`. They are:

    -  ``Name`` : The name of the column.

    -  ``DataType`` : The data type of the column.

    -  ``Width`` : The column width.

    -  ``NumberOfDecimals`` : The number of decimals of the column. Only
       applicable for numeric columns.

    -  ``IsPrimaryKey`` : Specfies whether the column is part of the primary
       key for the database table. Returns ``"Yes"`` or ``"No"``.

    -  ``Nullable`` : Specifies whether the column is nullable or not.
       Returns ``"Yes"`` or ``"No"``.

    -  ``DefaultValue`` : The default value of the column.

    -  ``Remark`` : The remark associated with the column.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The function :aimms:func:`SQLColumnData`.
