.. aimms:function:: me::Delete(runtimeId)

.. _me::Delete:

me::Delete
==========

The procedure :aimms:func:`me::Delete` a runtime identifier and all runtime
identifiers below that identifier.

.. code-block:: aimms

    me::Delete(
            runtimeId  ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

Return Value
------------

    Returns 1 if the delete operation is successful, 0 otherwise. In the
    latter case error(s) have been raised. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. seealso::

    -  The functions :aimms:func:`me::Children` and :aimms:func:`me::GetAttribute`.

    -  :doc:`Articles/146/146-value-dynamic-identifier`
       illustrates the use of model edit functions. The purpose of
       :aimms:func:`me::Delete` in that post is to remove an old existing library
       before creating a new one.
