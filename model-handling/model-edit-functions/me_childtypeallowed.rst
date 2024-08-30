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


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

Let ``ep_functionReferenceExampleRuntimeParameter`` have value ``frerl::p_a``, 
then the code:

.. code-block:: aimms

    _bp_childTypeAllowed := me::ChildTypeAllowed(
        runtimeId :  ep_functionReferenceExampleRuntimeParameter, 
        newType   :  'parameter');
    display _bp_childTypeAllowed ;

Produces the following in the listing file:

.. code-block:: aimms

    _bp_childTypeAllowed := 0 ;

Illustrating that a parameter cannot have, as child, another parameter.

References
-----------

    *   :aimms:func:`me::Create` 

    *   :aimms:func:`me::Children`

Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_


