.. aimms:function:: me::GetAttribute(runtimeId, attr)

.. _me::GetAttribute:

me::GetAttribute
================

The function :aimms:func:`me::GetAttribute` returns the contents of an attribute
as a string.

.. code-block:: aimms

    me::GetAttribute(
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

    Returns the contents of the attribute ``attr`` of runtime identifier
    ``runtimeId`` as a string. When ``runtimeId`` doesn't reference a
    runtime identifier an error will be raised.

.. seealso::

    The procedures :aimms:func:`AttributeToString`, :aimms:func:`me::SetAttribute` and :aimms:func:`me::Create`.
