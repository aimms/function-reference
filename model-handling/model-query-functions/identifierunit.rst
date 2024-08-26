.. aimms:function:: IdentifierUnit(identifierName)

.. _IdentifierUnit:

IdentifierUnit
==============

The function :aimms:func:`IdentifierUnit` returns the unit of ``identifierName``
as it is declared.

.. code-block:: aimms

    IdentifierUnit(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the unit should be obtained.

Return Value
------------

    This function returns a unit. If ``identifierName`` is not an
    identifier, an error message is issued. If ``identifierName`` is not a
    parameter, variable or constraint, the unit ``[]`` is returned without
    further warning.

.. note::

    This function complements the suffix :ref:`.unit`; when the unit of an
    identifier is a unit parameter, this function will return that unit
    parameter, whilst the suffix ``unit`` will return the value of that unit
    parameter.


Example
-------

Given the declaration: 

.. code-block:: aimms

	Parameter p_d {
		Unit: m;
	}

the code:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

	_ep_p := StringToElement(AllIdentifiers, 
		"chapterModel::sectionModelQuery::funcIdentifierUnit::p_d", 
		create: 0);
	_up_p := IdentifierUnit( _ep_p );
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _up_p ;
	endblock ;

produces in the listing file:

.. code-block:: aimms

    _up_p := [m] ;


References
-----------


    -  The functions :aimms:func:`IdentifierDimension` and :aimms:func:`IdentifierType`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The common example in :numref:`CommonModelQueryExample`.
