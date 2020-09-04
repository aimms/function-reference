.. aimms:function:: AttributeLength(IdentifierName, AttributeName)

.. _AttributeLength:

AttributeLength
=================

The function :aimms:func:`AttributeLength` returns the length of a string representation 
of a specified attribute for a given identifier.

.. code-block:: aimms

    AttributeLength(
         IdentifierName,       ! (input) scalar element parameter
         AttributeName         ! (input) scalar element parameter
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

.. seealso::

    The functions :aimms:func:`AttributeToString`, :aimms:func:`AttributeContainsString`.
