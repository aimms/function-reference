.. aimms:function:: me::Parent(runtimeId)

.. _me::Parent:

me::Parent
==========

The function :aimms:func:`me::Parent` returns the parent of a runtime identifier.

.. code-block:: aimms

    me::Parent(
            runtimeId   ! (input) an element
    )

Arguments
---------

    *runtimeId*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime identifier.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllIdentifiers` referencing the
    parent of the referenced identifier or the empty element if the
    referenced identifier is a runtime library. When ``runtimeId`` doesn't
    reference a runtime identifier an error will be raised.


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

Let 

*   ``ep_functionReferenceExampleRuntimeLib`` refer to the root of the runtime library, and

*   ``ep_functionReferenceExampleRuntimeProc`` refer to a procedure inside the library, then the code:

.. code-block:: aimms

    _ep_parent := me::Parent( ep_functionReferenceExampleRuntimeProc );

    display _ep_parent ;

produces the following in the listing file:

.. code-block:: aimms

    _ep_parent := 'FunctionReferenceExampleRuntimeLibrary' ;

References
-----------

    *   :aimms:func:`me::Children` 

    *   :aimms:func:`me::GetAttribute`.

Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_

