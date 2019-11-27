.. aimms:set:: AllColumnTypes

.. _AllColumnTypes:

AllColumnTypes
==============

The predefined set :aimms:set:`AllColumnTypes` contains the names of all column
types available in the matrix manipulation library of AIMMS.

.. code-block:: aimms

        Set AllColumnTypes {
            Index      :  IndexColumnTypes;
            Definition :  data { integer, continuous };
        }

Definition
----------

    The set :aimms:set:`AllColumnTypes` contains the names of all column types
    available in the matrix manipulation library of AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    ELement parameters into :aimms:set:`AllColumnTypes` can be used as the *type*
    argument of the :aimms:func:`GMP::Column::SetType` function.

.. seealso::

    The function :aimms:func:`GMP::Column::SetType`. Matrix manipulation is discussed in more detail
    in Chapter 16 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
