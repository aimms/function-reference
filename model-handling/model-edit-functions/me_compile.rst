.. aimms:function:: me::Compile(runtimeId)

.. _me::Compile:

me::Compile
===========

The procedure :aimms:func:`me::Compile` compiles a runtime identifier and all
runtime identifiers below that identifier. If that runtime identifier is
a runtime library, all procedures can be run and set / parameter
definitions can be evaluated provided there are no errors.

.. code-block:: aimms

    me::Compile(
            runtimeId  ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

Return Value
------------

    Returns 1 if the compilation operation is successful, 0 otherwise. In
    the latter case error(s) have been raised. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.

.. seealso::

    -  The functions :aimms:func:`me::IsRunnable` and the ``APPLY statement``, 
       see Section 10.3.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  :doc:`.../Articles/146/146-value-dynamic-identifier`
       illustrates the use of model edit functions. The purpose of
       :aimms:func:`me::Compile` in that post is to check the code in the runtime
       library and prepare it for execution.
