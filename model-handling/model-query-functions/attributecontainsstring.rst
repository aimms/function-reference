.. aimms:function:: AttributeContainsString(IdentifierName, AttributeName, Key)

.. _AttributeContainsString:

AttributeContainsString
========================

The function :aimms:func:`AttributeContainsString` returns 1 if the string representation of a specified attribute for a
given identifier contains the specified text (case sensitive).

.. code-block:: aimms

    AttributeContainsString(
         IdentifierName,       ! (input) scalar element parameter
         AttributeName         ! (input) scalar element parameter
         Key                   ! (input) scalar string expression
         )

Arguments
---------

    *IdentifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier.

    *AttributeName*
        An element expression in the predefined set :aimms:set:`AllAttributeNames` specifying the
        attribute.

    *Key*
        A string specifying the text to search for.

Return Value
------------

    1 if the attribute text contains the Key string (always case sensitive), 0 otherwise. In case of failure, the return value is 0 and the predeclared identifier
    :aimms:set:`CurrentErrorMessage` contains an appropriate error message.


Example
-------

Given the declaration:

.. code-block:: aimms

    Parameter p {
        Comment: "Hello";
    }

inside the nested module ``chapterModel::sectionModelQuery::funcAttributeLength``, 
the code that queries the comment attribute of identifier ``p`` is:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4-7

	_ep_p := StringToElement(AllIdentifiers, 
		"chapterModel::sectionModelQuery::funcAttributeLength::p", 
		create: 0);
	_bp_loPresent := AttributeContainsString(
		IdentifierName :  _ep_p, 
		AttributeName  :  'comment', 
		Key            :  "lo") ;
	block where single_column_display := 1, listing_number_precision := 6 ;
		display { _ep_p, _bp_loPresent };
	endblock ;

Remark: 

    *   Lines 1-3: Note that the name of the identifier contains all prefixes of the modules it is in.
    
The results in the listing file:  

.. code-block:: aimms

    _ep_p         := 'chapterModel::sectionModelQuery::funcAttributeLength::p' ;
    _bp_loPresent :=                                                         1 ;
      

References
-----------

    *   :aimms:func:`AttributeToString`, 
	
	*   :aimms:func:`AttributeLength`, 

    *	:aimms:func:`me::GetAttribute`.
