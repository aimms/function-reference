.. aimms:function:: me::IsRunnable(runtimeId)

.. _me::IsRunnable:

me::IsRunnable
==============

The function :aimms:func:`me::IsRunnable` determines whether or not the runtime
identifier resides in a runtime library for which all procedures are
runnable and all definitions can be evaluated.

.. code-block:: aimms

    me::IsRunnable(
            runtimeId   ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

Return Value
------------

    The function returns 1 iff ``runtimeId`` resides in a runtime library
    where all procedures are runnable and all definitions can be evaluated.
    When ``runtimeId`` doesn't reference a runtime identifier an error will
    be raised.

.. seealso::

    - The functions :aimms:func:`me::Compile` and :aimms:func:`me::IsReadonly`.
