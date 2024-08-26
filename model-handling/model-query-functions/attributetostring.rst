.. aimms:function:: AttributeToString(IdentifierName, AttributeName)

.. _AttributeToString:

AttributeToString
=================

The function :aimms:func:`AttributeToString` converts a specified attribute for a
given identifier to a string.

.. code-block:: aimms

    AttributeToString(
         IdentifierName,       ! (input) scalar element parameter
         AttributeName         ! (input) scalar element parameter
         )

Arguments
---------

    *IdentifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which an attribute should be converted to a string.

    *AttributeName*
        An element expression in the predefined set :aimms:set:`AllAttributeNames` specifying the
        attribute that should be converted to string format.

Return Value
------------

    This function returns a string representation of the attribute on
    success or the empty string otherwise and the predeclared identifier
    :aimms:set:`CurrentErrorMessage` contains an appropriate error message.

.. note::

    In order to protect the intellectual property of the model developer,
    the string ``Encrypted`` is returned and the predeclared identifier
    :aimms:set:`CurrentErrorMessage` contains an appropriate error message, when the identifier is
    in an encrypted section of the model. There is one exception; if the
    procedure making the call ``AttributeToString(id,attr)`` is in the same
    component as the identifier ``id``, the attribute ``attr`` is still
    returned as string. Here component is the main model or one of the
    libraries.





Example
-------

Given the declaration:

.. code-block:: aimms

    Parameter p {
        Comment: "Hello";
    }

inside the nested module ``chapterModel::sectionModelQuery::funcAttributeToString``, 
the code that queries the comment attribute of identifier ``p`` is:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

    _ep_p := StringToElement(AllIdentifiers, 
        "chapterModel::sectionModelQuery::funcAttributeToString::p", 
        create: 0);
    _sp_cmt := AttributeToString(_ep_p, 'comment');
    block where single_column_display := 1, listing_number_precision := 6 ;
        display { _ep_p, _sp_cmt };
    endblock ;

Remark: 

    *   Lines 1-3: Note that the name of the identifier contains all prefixes of the modules it is in.
    
The results in the listing file:  

.. code-block:: aimms

    _ep_p   := 'chapterModel::sectionModelQuery::funcAttributeToString::p' ;
    _sp_cmt :=                                                   "Hello\n" ;
      

References
-----------

    *   :aimms:func:`StringToElement`, 

    *   :aimms:func:`me::GetAttribute`, 

    *   :aimms:func:`AttributeContainsString`, and

    *   :aimms:func:`AttributeLength`.
