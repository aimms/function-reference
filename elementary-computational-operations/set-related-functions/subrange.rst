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


Example
-----------

Given the declarations:

.. code-block:: aimms


	Set s_products;
	Set s_youngProducts {
		SubsetOf: s_products;
	}

The statements

.. code-block:: aimms

	sp_products := SetAsString( s_products );
	sp_youngProducts := SetAsString( s_youngProducts );

	display sp_products, sp_youngProducts ;


will produce the following in the listing file:

.. code-block:: aimms

    s_products := data { p0, p1, p2, p3, p4 } ;
    s_youngProducts := data { p2, p3, p4 } ;
