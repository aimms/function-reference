.. aimms:function:: me::AllowedAttribute(runtimeId, attr)

.. _me::AllowedAttribute:

me::AllowedAttribute
====================

The function :aimms:func:`me::AllowedAttribute` returns 1 if the attribute is
allowed for the runtime id.

.. code-block:: aimms

    me::AllowedAttribute(
            runtimeId,  ! (input) an element
            attr        ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *attr*
        An element in the set :aimms:set:`AllAttributeNames`

Return Value
------------

    Returns 1 if the attribute ``attr`` of runtime identifier ``runtimeId`` is allowed. 
	When ``runtimeId`` doesn't reference a runtime identifier an error will be raised.


Example
-------

The code:

.. code-block:: aimms

    _bp_isAllowedAttribute := me::AllowedAttribute('webui_runtime::AllImplicitPublicIdentifiers','text');
    display _bp_isAllowedAttribute ;

produces in the listing file:

.. code-block:: aimms

    _bp_isAllowedAttribute := 1 ;

References
-----------

    *   :aimms:func:`IsRuntimeIdentifier`

    *   :aimms:func:`me::SetAttribute` 

    *   :aimms:func:`me::Create`.

Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_