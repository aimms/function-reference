.. aimms:function:: me::SetAttribute(runtimeId, attr, txt)

.. _me::SetAttribute:

me::SetAttribute
================

The procedure :aimms:func:`me::SetAttribute` changes the contents 
of an attribute of a runtime identifier.

.. code-block:: aimms

    me::SetAttribute(
            runtimeId,  ! (input) an element
            attr,       ! (input) an element
            txt         ! (input) a string expression
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *attr*
        An element in the set :aimms:set:`AllAttributeNames`.

    *txt*
        The text to be assigned. Using the empty string will effectively delete
        the attribute from the runtime identifier.

Return Value
------------

    Returns 1 if the text assignment to the attribute is successful, 0
    otherwise. In the latter case error(s) have been raised. When
    ``runtimeId`` doesn't reference a runtime identifier an error will be
    raised.


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

|

Let 

*   ``ep_functionReferenceExampleRuntimeParameter`` refer to the parameter in the runtime library, then the code:

.. code-block:: aimms

	me::SetAttribute(
		runtimeId :  ep_functionReferenceExampleRuntimeParameter, 
		attr      :  'text', 
		txt       :  "just another runtime identifier");
	_sp_text := me::GetAttribute(
		runtimeId :  ep_functionReferenceExampleRuntimeParameter, 
		attr      :  'text');
	display _sp_text ;

produces the following in the listing file:

.. code-block:: aimms

    _sp_text := "just another runtime identifier" ;

.. seealso::

    - :aimms:func:`me::ChangeType`.
    - :aimms:func:`me::Rename`.
    - Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_.
