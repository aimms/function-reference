.. aimms:procedure:: RestoreInactiveElements(SearchSet, SearchIdentifiers, UsedElements)

.. _RestoreInactiveElements:

RestoreInactiveElements
=======================

The procedure :aimms:procedure:`RestoreInactiveElements` finds and restores all
elements that were previously removed from a particular set, but for
which inactive data still exists in a given collection of indexed model
identifiers.

.. code-block:: aimms

    RestoreInactiveElements(
         SearchSet,          ! (input/output) a set
         SearchIdentifiers,  ! (input) a subset of AllIdentifiers
         UsedElements        ! (output) a subset
         )

Arguments
---------

    *SearchSet*
        The set for which you want to find the inactive elements.

    *SearchIdentifiers*
        A subset of :aimms:set:`AllIdentifiers`, holding identifiers that are indexed over
        *SearchSet*.

    *UsedElements*
        A subset of *SearchSet*. On return this subset will contain all the
        inactive elements that are currently used (i.e. have corresponding
        nondefault values) in the identifiers contained in *SearchIdentifiers*.

.. note::

    The inactive elements found are placed in the *result-set*, but are also
    automatically added to the *search-set*.





Example
-----------

Given the declarations:

.. code-block:: aimms

	Set s_products {
		Index: i_prod;
	}
	Parameter p_rev {
		IndexDomain: i_prod;
	}
	Set s_searchIds {
		SubsetOf: AllIdentifiers;
	}
	Set s_restoredProducts {
		SubsetOf: s_products;
	}


The code

.. code-block:: aimms

	! a bit of data.
	s_products := ElementRange(0,9,prefix:"p");
	p_rev(i_prod) := data { 
		p1 : 7,  p2 : 9,  p3 : 9,  
		p6 : 8,  p7 : 6,  p8 : 8 } ;

	! Remove some elements from root set.
	s_products -= data { p3, p4, p8, p9 } ;

	! Display resulting data 
	display s_products ; ! s_products := data { p0, p1, p2, p5, p6, p7 } ;
	display p_rev ; ! p_rev := data { p1 : 7,  p2 : 9,  p6 : 8,  p7 : 6 } ;
	! p_rev only has 4 elements left; some elements of p_rev seem to have disappeared; 
	! These elements are called the inactive elements of p_rev.

	! Search for inactive products that have a revenue, and restore 
	! the corresponding elements to active.
	s_searchIds := data { p_rev } ;
	RestoreInactiveElements(
		SearchSet         :  s_products, 
		SearchIdentifiers :  s_searchIds, 
		UsedElements      :  s_restoredProducts);
	display s_restoredProducts ; ! s_restoredProducts := data { p3, p8 } ;
	display s_products ; ! s_products := data { p0, p1, p2, p3, p5, p6, p7, p8 } ;
	! The previously inactive data of p_rev is now active again:
	display p_rev ; ! p_rev := data { p1 : 7,  p2 : 9,  p3 : 9,  p6 : 8,  p7 : 6,  p8 : 8 } ;

See also:

	-   The function :aimms:set:`ActiveCard`.
	
	-	The explanation of inactive elements in the Language Reference at :ref:`inactive_data`.
	
	-	The AIMMS Developer tool Identifier Cardinalities, see :ref:`sec:debug.card`.