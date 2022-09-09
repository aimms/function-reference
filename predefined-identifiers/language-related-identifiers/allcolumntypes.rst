.. aimms:set:: AllColumnTypes

.. _AllColumnTypes:

AllColumnTypes
==============

The predefined set :aimms:set:`AllColumnTypes` contains the names of all column
types available in the GMP library of AIMMS.

.. code-block:: aimms

        Set AllColumnTypes {
            Index      :  IndexColumnTypes;
            Definition :  data { integer, continuous };
        }

Definition
----------

    The set :aimms:set:`AllColumnTypes` contains the names of all column types
    available in the GMP library of AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`AllColumnTypes` can be used as the *type*
    argument of the :aimms:func:`GMP::Column::SetType` function.

.. seealso::

    The function :aimms:func:`GMP::Column::SetType`. The GMP library is discussed in more detail
    in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
