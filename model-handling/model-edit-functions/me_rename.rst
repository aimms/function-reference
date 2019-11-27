.. aimms:function:: me::Rename(runtimeId, newname)

.. _me::Rename:

me::Rename
==========

The procedure :aimms:func:`me::Rename` renames a runtime identifier. In addition,
all text within the runtime library referencing that runtime identifier
will be adapted accordingly.

.. code-block:: aimms

    me::Rename(
            runtimeId,  ! (input) an element
            newname     ! (input) a string
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *newname*
        A string.

Return Value
------------

    Returns 1 if the rename operation is successful, 0 otherwise. In the
    latter case error(s) have been raised. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. note::

    The name change file is not supported for runtime libraries.

.. seealso::

    The functions :aimms:func:`me::ChangeType` and :aimms:func:`me::Move`.
