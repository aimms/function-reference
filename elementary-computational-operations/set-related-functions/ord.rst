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

Example
-----------

Given the declarations:

.. code-block:: aimms

	Set s_products {
		Index: i_prod;
		Definition: ElementRange(0,9,prefix:"p");
	}
	Set s_topProducts {
		SubsetOf: s_products;
		Index: i_topProd;
		OrderBy: user;
	}
	Parameter p_rev {
		IndexDomain: i_prod;
	}
	ElementParameter ep_p5 {
		Range: s_products;
	}
	Parameter p_ordP5;
	Parameter p_ordP5top;

The code:

.. code-block:: aimms

	! a bit of data.
	p_rev(i_prod) := data { 
		p0 : 3,  p1 : 7,  p2 : 9,  p3 : 9,  p4 : 3,  
		p5 : 4,  p6 : 8,  p7 : 6,  p8 : 8,  p9 : 7 } ;

	! Sorting on revenue, note that s_topProducts has order by: user.
	s_topProducts := sort(i_prod, -p_rev(i_prod) );

	! Getting the position in the set of element p5
	ep_p5 := 'p5' ;
	p_ordP5 := ord( ep_p5 ); ! The position of 'p5' in set s_products is 6.
	p_ordP5top := ord( ep_p5, s_topProducts ); ! The position of 'p5' in set s_topProducts is 8.

Shows the use of adding a set to the function `Ord`.
 
