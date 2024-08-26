.. aimms:function:: AttributeLength(IdentifierName, AttributeName)

.. _AttributeLength:

AttributeLength
=================

The function :aimms:func:`AttributeLength` returns the length of a string representation 
of a specified attribute for a given identifier.

.. code-block:: aimms

    AttributeLength(
         IdentifierName,  ! (input) scalar element parameter
         AttributeName    ! (input) scalar element parameter
         )

Arguments
---------

    *IdentifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which an attribute length has to be returned.

    *AttributeName*
        An element expression in the predefined set :aimms:set:`AllAttributeNames` specifying the
        attribute.

Return Value
------------

    This function returns the length of a string representation of the attribute on
    success or zero otherwise and the predeclared identifier
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
    :emphasize-lines: 4

    _ep_p := StringToElement(AllIdentifiers, 
        "chapterModel::sectionModelQuery::funcAttributeLength::p", 
        create: 0);
    _p_cmt := AttributeLength(_ep_p, 'comment');
    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _ep_p, _p_cmt };
    endblock ;

Remark: 

    *   Lines 1-3: Note that the name of the identifier contains all prefixes of the modules it is in.
    
The results in the listing file:  

.. code-block:: aimms

    _ep_p  := 'chapterModel::sectionModelQuery::funcAttributeLength::p' ;
    _p_cmt :=                                                         5 ;
      

References
-----------

    *   :aimms:func:`AttributeToString`, 
    
    *   :aimms:func:`AttributeContainsString`.
