.. aimms:function:: SetAsString(set)

.. _SetAsString:

SetAsString
===========

With the function :aimms:func:`SetAsString` you can cast a set expression to a string.

.. code-block:: aimms

    SetAsString(
         set             ! (input) a set expression
         )

Arguments
---------

    *set*
        A set for which you want to get a string representation.

Return Value
------------

    The function returns the string representation of the given set, 
    being elements of the set separated by commas and enclosed in curly brackets.
    If the set is empty then the strings is just curly brackets, like so ``'{}'``.


.. note::

    This function is available since AIMMS version 4.89.
    
    Implicit cast from a set expression to a string is decommissioned since AIMMS version 4.89 and will result in a compile error in a future AIMMS version. :aimms:func:`SetAsString` function is intended to be used instead.


Example
-----------

Given the declarations:

.. code-block:: aimms

	Set s_products {
		Index: i_prod;
	}
	Set s_productGroups {
		Index: i_pg;
		Definition: data { fast, slow };
	}
	Set s_productsByGroup {
		IndexDomain: i_pg;
		SubsetOf: s_products;
	}
	StringParameter sp_productGroup {
		IndexDomain: i_pg;
	}

With the data:

.. code-block:: aimms


	! A bit of data
	s_products := elementRange(1,4,prefix:"p");
	s_productsByGroup(i_pg) := data {
		fast : { p3, p4 },
		slow : { p1, p2 }
	} ;

The code:

.. code-block:: aimms

	sp_productGroup(i_pg) := SetAsSTring( s_productsByGroup(i_pg) );
	block where single_column_display := 1;
		display sp_productGroup ;
	endblock ;

Produces

.. code-block:: aimms

    elementary::setop::funcSetAsString::sp_productGroup := data 
    { fast : "{ p3, p4 }",
      slow : "{ p1, p2 }" } ;

in the listing file.