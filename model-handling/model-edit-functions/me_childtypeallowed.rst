.. aimms:function:: me::ChildTypeAllowed(runtimeId, newType)

.. _me::ChildTypeAllowed:

me::ChildTypeAllowed
====================

The function :aimms:func:`me::ChildTypeAllowed` returns 1 if a child of type
``newType`` can be added as a child to runtime identifier
``runtimeId``..

.. code-block:: aimms

    me::ChildTypeAllowed(
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

    Returns 1 if the identifier of type ``newType`` can be added as a child
    to identifier ``runtimeId``. When ``runtimeId`` doesn't reference a
    runtime identifier an error will be raised.

.. seealso::

    The functions :aimms:func:`me::Create` and :aimms:func:`me::Move`.
