.. aimms:function:: me::ChangeType(runtimeId, newType)

.. _me::ChangeType:

me::ChangeType
==============

The procedure :aimms:func:`me::ChangeType` changes the type of a runtime
identifier.

.. code-block:: aimms

    me::ChangeType(
            runtimeId,  ! (input) an element
            newType     ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *newType*
        An element in the set :aimms:set:`AllIdentifierTypes`.

Return Value
------------

    Returns 1 if the change type operation is successful, 0 otherwise. In
    the latter case error(s) have been raised. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. seealso::

    The functions :aimms:func:`me::Create` and :aimms:func:`me::Move`.
