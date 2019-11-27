.. aimms:function:: me::ChangeTypeAllowed(runtimeId, newType)

.. _me::ChangeTypeAllowed:

me::ChangeTypeAllowed
=====================

The function :aimms:func:`me::ChangeTypeAllowed` returns 1 if the type of runtime
identifier ``runtimeId`` can be changed into type ``newType``.

.. code-block:: aimms

    me::ChangeTypeAllowed(
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

    Returns 1 if the identifier ``runtimeId`` can be changed into
    ``newType``. When ``runtimeId`` doesn't reference a runtime identifier
    an error will be raised.

.. seealso::

    The functions :aimms:func:`me::Create` and :aimms:func:`me::Move`.
