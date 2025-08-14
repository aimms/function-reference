.. aimms:procedure:: FindUsedElements(SearchSet, SearchIdentifiers, UsedElements)

.. _FindUsedElements:

FindUsedElements
================

The procedure :aimms:procedure:`FindUsedElements` finds all elements of a particular
set that are in use in a given collection of indexed model identifiers.

.. code-block:: aimms

    FindUsedElements(
         SearchSet,           ! (input) a set
         SearchIdentifiers,   ! (input) a subset of AllIdentifiers
         UsedElements         ! (output) a subset
         )

Arguments
---------

    *SearchSet*
        The set for which you want to find the used elements.

    *SearchIdentifiers*
        A subset of :aimms:set:`AllIdentifiers`, holding identifiers that are indexed over
        ``SearchSet``.

    *UsedElements*
        A subset of *SearchSet*. On return this subset will contain the elements
        that are currently used (i.e. have corresponding nondefault values) in
        the identifiers contained in *SearchIdentifiers*.


Example
-----------

Given declarations:

.. code-block:: aimms

	Set s_time {
		Index: i_t;
	}
	Set s_products {
		Index: i_prod;
	}
	Set s_productsAvailable {
		SubsetOf: s_products;
	}
	Set s_productsRequired {
		SubsetOf: s_products;
	}
	Set s_productsRequiredNotAvailable {
		SubsetOf: s_products;
	}
	Set s_supplyIds {
		SubsetOf: AllIdentifiers;
		Definition: Supply_data;
		Comment: "The identifiers stocking or supplying products.";
	}
	Set s_demandIds {
		SubsetOf: AllIdentifiers;
		Definition: Demand_data;
		Comment: "The identifiers requiring products";
	}
	DeclarationSection Supply_data {
		Parameter p_stock {
			IndexDomain: i_prod;
		}
		Parameter p_production {
			IndexDomain: (i_prod,i_t);
		}
	}
	DeclarationSection Demand_data {
		Parameter p_demand {
			IndexDomain: i_prod;
		}
	}

Specifying a bit of data: 

.. code-block:: aimms

    ! Get some sample data
    s_time := elementRange(1,3, prefix: "t" );
    s_products := ElementRange( 1, 5, prefix: "p" );
    p_stock(i_prod) := data { p2 : 3, p3 : 5 } ;
    p_production(i_prod,i_t) := data {
        ( p1, t1 ) : 4,
        ( p2, t2 ) : 3 } ;
    p_demand(i_prod) := data { p1 : 3, p2 : 3, p4 : 3, p5 : 3 } ;
    
Then the code:

.. code-block:: aimms

    ! Find the products that are on stock or can be produced:
    FindUsedElements(
        SearchSet         :  s_products, 
        SearchIdentifiers :  s_supplyIds, 
        UsedElements      :  s_productsAvailable);

    ! Find the products that are in demand:
    FindUsedElements(
        SearchSet         :  s_products, 
        SearchIdentifiers :  s_demandIds, 
        UsedElements      :  s_productsRequired);

    display s_productsAvailable, s_productsRequired ;

Will produce:

.. code-block:: aimms

    s_productsAvailable := data { p1, p2, p3 } ;

    s_productsRequired := data { p1, p2, p4, p5 } ;

in the listing file. 

And the code

.. code-block:: aimms

    ! Check if we require products that are not available.
    s_productsRequiredNotAvailable := 
        s_productsRequired - s_productsAvailable ;
    if card( s_productsRequiredNotAvailable ) then
        raise error formatString(
            "The products %s are required, but cannot be made available", 
            setAsString( s_productsRequiredNotAvailable ) );
    endif ;
    

will raise the error:

.. code-block:: aimms

    The products { p4, p5 } are required, but cannot be made available.

.. seealso::

    -   `Data control function <https://documentation.aimms.com/language-reference/data-communication-components/data-initialization-verification-and-control/data-control.html#data-control>`_