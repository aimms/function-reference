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

.. seealso::

    The function :aimms:func:`me::GetAttribute`.
