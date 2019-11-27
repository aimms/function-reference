.. aimms:function:: me::Parent(runtimeId)

.. _me::Parent:

me::Parent
==========

The function :aimms:func:`me::Parent` returns the parent of a runtime identifier.

.. code-block:: aimms

    me::Parent(
            runtimeId   ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllIdentifiers` referencing the
    parent of the referenced identifier or the empty element if the
    referenced identifier is a runtime library. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. seealso::

    The functions :aimms:func:`me::Children` and :aimms:func:`me::GetAttribute`.
