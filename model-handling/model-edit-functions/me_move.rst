.. aimms:function:: me::Move(runtimeId, parentid, pos)

.. _me::Move:

me::Move
========

The procedure :aimms:func:`me::Move` renames a runtime identifier. In addition,
when the move changes the namespace of the runtime identifier all text
within the runtime library referencing that runtime identifier will be
adapted accordingly.

.. code-block:: aimms

    me::Move(
            runtimeId,  ! (input) an element
            parentid,   ! (input) an element
            pos         ! (input) integer
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *parentid*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifeir in the
        same runtime library.

    *pos*
        An integer position in the section. 1 is the first position, and 0 means
        "place at end".

Return Value
------------

    Returns 1 if the move operation is successful, 0 otherwise. In the
    latter case error(s) have been raised. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. note::

    The name change file is not supported for runtime libraries.

.. seealso::

    The functions :aimms:func:`me::ChangeType` and :aimms:func:`me::Rename`.
