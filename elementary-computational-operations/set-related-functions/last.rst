.. aimms:function:: Last(Set)

.. _Last:

Last
====

With the function :aimms:func:`Last` you can retrieve the last element from a set.

.. code-block:: aimms

    Last(
           Set,             ! (input) set reference
        )

Arguments
---------

    *Set*
        The set from which the last element is to be returned.

Return Value
------------

    The function Last returns the last element of set *Set*.

.. note::

    If there is no element in *Set*, the function returns the empty element
    ``''`` instead.


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
	ElementParameter ep_lastProd {
		Range: s_products;
	}
	ElementParameter ep_theBottomProd {
		Range: s_products;
	}

The code:

.. code-block:: aimms

	! a bit of data.
	p_rev(i_prod) := data { 
		p0 : 3,  p1 : 7,  p2 : 9,  p3 : 9,  p4 : 3,  
		p5 : 4,  p6 : 8,  p7 : 6,  p8 : 8,  p9 : 7 } ;

	! Sorting on revenue, note that s_topProducts has order by: user.
	s_topProducts := sort( i_prod, -p_rev(i_prod) );

	! Getting the first of both sets.
	ep_lastProd := last( s_products );
	ep_theBottomProd := last( s_topProducts );

	! Printing to listing file.
	display s_topProducts, ep_lastProd, ep_theBottomProd ;

produces 

.. code-block:: aimms

    s_topProducts := data { p2, p3, p6, p8, p1, p9, p7, p5, p0, p4 } ;

    ep_lastProd := 'p9' ;

    ep_theBottomProd := 'p4' ;

in the listing file.


