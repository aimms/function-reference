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



Example
-------

Viewing a small runtime library defined as:

.. code-block:: aimms

    LibraryModule FunctionReferenceExampleRuntimeLibrary {
        Prefix: frerl;
        DeclarationSection runtime_declaration_identifiers {
            Parameter p_a;
        }
        Procedure runtimeProc {
            Body: {
                display p_a;
            }
        }
    }

Then the code:

.. code-block:: aimms

    me::Compile( ep_functionReferenceExampleRuntimeLib );
    apply( ep_functionReferenceExampleRuntimeProc );

Produces the following in the listing file:

.. code-block:: aimms

    frerl::p_a := 0 ;

This is an illustration of the best practice to compile an entire runtime library,
before executing a procedure instide that library.

References
-----------

    *   :aimms:func:`me::SetAttribute` 

    *   :aimms:func:`me::Create`.

    *   :aimms:func:`me::IsRunnable` 

    *   The ``APPLY statement``, see :ref:`sec:intern.ref.apply` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_


