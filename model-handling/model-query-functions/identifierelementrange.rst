.. aimms:function:: IdentifierElementRange(identifierName)

.. _IdentifierElementRange:

IdentifierElementRange
======================

The function :aimms:func:`IdentifierElementRange` returns the range as a set.

.. code-block:: aimms

    IdentifierElementRange(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllSymbols` specifying the
        identifier for which the range should be obtained.

Return Value
------------

    This function returns the set, as an element in :aimms:set:`AllSymbols`, that is the
    range of ``identifierName`` if it is element valued. If
    ``identifierName`` is not an identifier, an error message is issued. If
    ``identifierName`` is not element valued, the empty element is returned
    without further warning.

Example
-------

Given the declaration: 


.. code-block:: aimms

	Set s_a;
	ElementParameter ep_d {
		Range: s_a;
	}

the code:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

	_ep_p := StringToElement(AllIdentifiers, 
		"chapterModel::sectionModelQuery::funcIdentifierElementRange::ep_d", 
		create: 0);
	_ep_s := IdentifierElementRange( _ep_p );
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _ep_s ;
	endblock ;

produces in the listing file:

.. code-block:: aimms

    _ep_s := 'chapterModel::sectionModelQuery::funcIdentifierElementRange::s_a' ;


.. seealso::

    -  The functions :aimms:func:`DomainIndex`, :aimms:func:`IdentifierDimension`, and :aimms:func:`IndexRange`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.