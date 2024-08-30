.. aimms:function:: me::Children(runtimeId, runtimeChildren)

.. _me::Children:

me::Children
============

The procedure :aimms:func:`me::Children` returns the number of children of a
runtime identifier and fills an output parameter with those children.

.. code-block:: aimms

    me::Children(
            runtimeId,          ! (input) an element
            runtimeChildren(i)  ! (output) indexed element parameter.
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

    *runtimeChildren*
        The children in the runtime identifier tree. This parameter needs to be
        an output parameter indexed over a (subset of) the set :aimms:set:`Integers`.

Return Value
------------

    This procedure returns the number of children of ``runtimeId``. When
    ``runtimeId`` doesn't reference a runtime identifier an error will be
    raised.


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

Let ``ep_functionReferenceExampleRuntimeLib`` have value ``FunctionReferenceExampleRuntimeLibrary``, 
then the code:

.. code-block:: aimms

	me::Children(
		runtimeId       :  ep_functionReferenceExampleRuntimeLib, 
		runtimeChildren :  _ep_children);
	block where single_column_display := 1, listing_number_precision := 6 ;
		display _ep_children ;
	endblock ;

produces in the listing file:

.. code-block:: aimms

    _ep_children := data 
    { 1 : 'frerl::runtime_declaration_identifiers',
      2 : 'frerl::runtimeProc'                     } ;

Illustrating navigating from one runtime identifier to another using model edit functions.

References
-----------

    *   :aimms:func:`me::Parent` 

    *   :aimms:func:`me::GetAttribute`.

Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_



