.. aimms:set:: AllRowTypes

.. _AllRowTypes:

AllRowTypes
===========

The predefined set :aimms:set:`AllRowTypes` contains the collection of all
possible row types and is the superset of .

.. code-block:: aimms

        Set AllRowTypes {
            Index      :  IndexRowTypes;
            Definition :  data { '<=', '=', '>=', ranged, '<', '>', '<>' };
        }

Definition
----------

    The set :aimms:set:`AllRowTypes` contains the collection of all possible row
    types available in the matrix manipulation library of AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`AllRowTypes` can be used as the *type*
    argument of the :aimms:func:`GMP::Row::SetType` function.

.. seealso::

    The function :aimms:func:`GMP::Row::SetType`. Matrix manipulation is discussed in more detail
    in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
