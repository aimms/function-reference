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
