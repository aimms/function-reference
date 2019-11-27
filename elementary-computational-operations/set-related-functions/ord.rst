.. aimms:function:: Ord(index[, set])

.. _Ord:

Ord
===

The function :aimms:func:`Ord` returns the ordinal number of a set element
relative to a set.

.. code-block:: aimms

    Ord(
       index,        ! (input) element expression
       [set]         ! (optional) set reference
       )

Arguments
---------

    *index*
        An element expression for which you want to obtain the ordinal number.

    *set (optional)*
        The set with respect to which you want the ordinal number to be taken.
        If omitted, *set* is assumed to be the range of the argument *index*.

Return Value
------------

    The function :aimms:func:`Ord` returns the ordinal number of *index* in set *set*.

.. note::

    A compile time error occurs if the argument *set* is not present, and
    AIMMS is unable to determine the range of *index*.
