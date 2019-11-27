.. aimms:function:: SubRange(Superset, First, Last)

.. _SubRange:

SubRange
========

The function :aimms:func:`SubRange` extracts a subrange of consecutive elements
from an existing set.

.. code-block:: aimms

    SubRange(
         Superset,      ! (input) a simple set
         First,         ! (input) an element
         Last           ! (input) an element
         )

Arguments
---------

    *Superset*
        The set containing the subrange of elements that you want to extract.

    *First*
        An element in *Superset* representing the first element of the subrange.

    *Last*
        An element in *Superset* representing the last element of the subrange.

Return Value
------------

    The function returns a set containing the subrange of elements extracted
    from *Superset*. If the element *First* is positioned after *Last*, then
    the empty set is returned.
