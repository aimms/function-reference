.. aimms:function:: StringToElement(Set, Name[, create])

.. _StringToElement:

StringToElement
===============

With the function :aimms:func:`StringToElement` you can convert a string into an
(existing) element of a set.

.. code-block:: aimms

    StringToElement(
         Set,             ! (input/output) a reference to a simple set
         Name,            ! (input) a scalar string
         [create]         ! (optional) 0 or 1, default 0
         )

Arguments
---------

    *Set*
        A set in which you want to find (or create) a specific element.

    *Name*
        A scalar string expression, representing the string that you want to
        convert.

    *create (optional)*
        An indicator whether or not a nonexisting element are added to the set
        during the call.

Return Value
------------

    The function returns the existing element or, if the string cannot be
    converted to an existing element and the argument *create* is not set to
    1, the function return the empty element. If *create* is set to 1,
    nonexisting elements will be created on the fly.



Example
-----------

Given the declarations:

.. code-block:: aimms


	Set s_products {
		Index: i_prod;
		Parameter: ep_p0, ep_p1, ep_p2;
	}


The statements

.. code-block:: aimms


	ep_p0 := StringToElement( s_products, "p0", create: 1);
	ep_p1 := StringToElement( s_products, "p1", create: 1);
	ep_p2 := StringToElement( s_products, "p2", create: 0);

	display s_products, ep_p0, ep_p1, ep_p2 ;


will produce the following in the listing file:

.. code-block:: aimms

    s_products := data { p0, p1 } ;
    ep_p0 := 'p0' ;
    ep_p1 := 'p1' ;
    ep_p2 := '' ;


As you can see, an element for ``p2`` was not created as the corresponding argument ``create`` was set to 0.

.. seealso::

    -  The function :aimms:func:`ElementCast` and the procedure :aimms:procedure:`SetElementAdd`.

    -  The lexical conventions for set elements in :doc:`preliminaries/language-preliminaries/lexical-conventions`.
