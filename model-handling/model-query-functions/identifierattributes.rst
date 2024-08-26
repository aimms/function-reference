.. aimms:function:: IdentifierAttributes(IdentifierName)

.. _IdentifierAttributes:

IdentifierAttributes
====================

The function :aimms:func:`IdentifierAttributes` determines which attributes a
specified identifier has.

.. code-block:: aimms

    IdentifierAttributes(
         IdentifierName       ! (input) scalar element parameter
         )

Arguments
---------

    *IdentifierName*
        An element expression specifying the identifier for which the attributes
        should be determined.

Return Value
------------

    This function returns a subset of :aimms:set:`AllAttributeNames` containing all the
    attributes for the specified identifier.


Example
-------

The code:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

	_ep_mp := StringToElement(AllIdentifiers, 
		"chapterModel::sectionModelQuery::funcIdentifierAttributes::mp_loc", 
		create: 0);
	_s_someAttributes := IdentifierAttributes( _ep_mp );
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _s_someAttributes  ;
	endblock ;

produces in the listing file:

.. code-block:: aimms

    _s_someAttributes := data 
    { comment            ,
      constraints        ,
      convention         ,
      direction          ,
      objective          ,
      text               ,
      type               ,
      variables          ,
      'violation penalty' } ;

 