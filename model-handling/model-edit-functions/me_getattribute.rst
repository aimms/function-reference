.. aimms:function:: me::GetAttribute(runtimeId, attr)

.. _me::GetAttribute:

me::GetAttribute
================

The function :aimms:func:`me::GetAttribute` returns the contents of an attribute
as a string.

.. code-block:: aimms

    me::GetAttribute(
            runtimeId,  ! (input) an element
            attr        ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *attr*
        An element in the set :aimms:set:`AllAttributeNames`.

Return Value
------------

    Returns the contents of the attribute ``attr`` of runtime identifier
    ``runtimeId`` as a string. When ``runtimeId`` doesn't reference a
    runtime identifier an error will be raised.


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

    _sp_body := me::GetAttribute(ep_functionReferenceExampleRuntimeProc,'body');
    display _sp_body ;

produces the following in the listing file:

.. code-block:: aimms

    _sp_body := "display p_a;\n" ;



.. seealso::

    - :aimms:func:`AttributeToString`.
    - :aimms:func:`me::SetAttribute`.
    - :aimms:func:`me::Create`.
    - Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_.
