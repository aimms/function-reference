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


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

Let ``ep_functionReferenceExampleRuntimeParameter`` have value ``frerl::p_a``, then the code

.. code-block:: aimms

    _bp_changeTypeAllowed := me::ChangeTypeAllowed( ep_functionReferenceExampleRuntimeParameter, 'quantity' );
    display _bp_changeTypeAllowed ;

produces in the listing file:

.. code-block:: aimms

    _bp_changeTypeAllowed := 0 ;

illustrating that a parameter cannot be changed into a quantity.

.. seealso::

    - :aimms:func:`me::ChangeType`.
    - :aimms:func:`IdentifierTYpe`.
    - Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_.