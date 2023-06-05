.. aimms:set:: AllRowColumnStatuses

.. _AllRowColumnStatuses:

AllRowColumnStatuses
====================

The predefined set :aimms:set:`AllRowColumnStatuses` contains the collection of all
possible row and column statuses.

.. code-block:: aimms

        Set AllRowColumnStatuses {
            Index      :  IndexRowColumnStatuses;
            Definition :  data { Active, Deactivated, Deleted, NotGenerated, PresolveDeleted };
        }

Definition
----------

    The set :aimms:set:`AllRowColumnStatuses` contains the collection of all possible row and
    column statuses available in the GMP library of AIMMS.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    The functions :aimms:func:`GMP::Column::GetStatus` and :aimms:func:`GMP::Row::GetStatus`
    return an element in :aimms:set:`AllRowColumnStatuses`.

.. seealso::

    The functions :aimms:func:`GMP::Column::GetStatus` and :aimms:func:`GMP::Row::GetStatus`. The GMP library is discussed in more detail
    in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
