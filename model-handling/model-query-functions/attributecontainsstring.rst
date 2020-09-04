.. aimms:function:: AttributeContainsString(IdentifierName, AttributeName, Key)

.. _AttributeContainsString:

AttributeContainsString
========================

The function :aimms:func:`AttributeContainsString` returns 1 if the string representation of a specified attribute for a
given identifier contains the specified text.

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

    1 if the attribute text contains the Key string, 0 otherwise. In case of failure, the return value is 0 and the predeclared identifier
    :aimms:set:`CurrentErrorMessage` contains an appropriate error message.

.. seealso::

    The functions :aimms:func:`AttributeToString`, :aimms:func:`AttributeLength`, function :aimms:func:`me::GetAttribute`.
