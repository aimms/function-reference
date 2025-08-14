.. aimms:procedure:: SetAddRecursive(toSet, fromSet)

.. _SetAddRecursive:

SetAddRecursive
===============

With the procedure :aimms:procedure:`SetAddRecursive` you can merge the elements of one
set into another set.

.. code-block:: aimms

    SetAddRecursive(
         toSet,             ! (input/output) a set
         fromSet            ! (input) a set
         )

Arguments
---------

    *toSet*
        The set into which the elements of *fromSet* are merged.

    *fromSet*
        The set that you want to merge in *toSet*.

.. note::

    -  The sets *toSet* and *fromSet* should have the same root set.

    -  The difference between this function and a regular set assignment is
       that in case *fromSet* is not the domain of *toSet* all elements
       added to *toSet* will also be added to the domain set of *toSet*.

Example
-----------

Given the declarations:

.. code-block:: aimms


	Set s_products {
		Index: i_prod;
	}
	Set s_allActiveProducts {
		SubsetOf: s_products;
	}
	Set s_fastMovingProducts {
		SubsetOf: s_allActiveProducts;
	}
	Set s_newFastMovingProducts {
		SubsetOf: s_products;
	}

and a bit of initial data

.. code-block:: aimms

	! A bit of data
	s_products := ElementRange(0,9,prefix:"p");
	s_allActiveProducts := subrange( s_products, 'p2', 'p7' );
	s_fastMovingProducts := subrange( s_allActiveProducts, 'p4', 'p7' );
	s_newFastMovingProducts := subrange( s_products, 'p6', 'p9' );

the display statement

.. code-block:: aimms

	display s_products, s_allActiveProducts, s_fastMovingProducts, s_newFastMovingProducts ;

produces:

.. code-block:: aimms

    s_products := data { p0, p1, p2, p3, p4, p5, p6, p7, p8, p9 } ;
    s_allActiveProducts := data { p2, p3, p4, p5, p6, p7 } ;
    s_fastMovingProducts := data { p4, p5, p6, p7 } ;
    s_newFastMovingProducts := data { p6, p7, p8, p9 } ;


After applying ``SetAddRecursive``:
	
.. code-block:: aimms

	SetAddRecursive(
		toSet   :  s_fastMovingProducts, 
		fromSet :  s_newFastMovingProducts);

The display statement

.. code-block:: aimms

	display s_products, s_allActiveProducts, s_fastMovingProducts, s_newFastMovingProducts ;

produces:

.. code-block:: aimms

    s_products := data { p0, p1, p2, p3, p4, p5, p6, p7, p8, p9 } ;
    s_allActiveProducts := data { p2, p3, p4, p5, p6, p7, p8, p9 } ;
    s_fastMovingProducts := data { p4, p5, p6, p7, p8, p9 } ;
    s_newFastMovingProducts := data { p6, p7, p8, p9 } ;
	
As you can see, the elements ``p8`` and ``p9``, are added both to ``s_fastMovingProducts`` 
and its domain set ``s_allActiveProducts``.