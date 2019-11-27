.. aimms:function:: me::AllowedAttribute(runtimeId, attr)

.. _me::AllowedAttribute:

me::AllowedAttribute
====================

The function :aimms:func:`me::AllowedAttribute` returns 1 if the attribute is
allowed for the runtime id.

.. code-block:: aimms

    me::AllowedAttribute(
            runtimeId,  ! (input) an element
            attr        ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *attr*
        An element in the set :aimms:set:`AllAttributeNames`

Return Value
------------

    Returns 1 if the attribute ``attr`` of runtime identifier ``runtimeId``
    is allowed. When ``runtimeId`` doesn't reference a runtime identifier an
    error will be raised.

.. seealso::

    The procedures :aimms:func:`me::SetAttribute` and :aimms:func:`me::Create`.
