.. aimms:function:: IsRuntimeIdentifier(identifierName)

.. _IsRuntimeIdentifier:

IsRuntimeIdentifier
===================

The function :aimms:func:`IsRuntimeIdentifier` returns 1 when the argument
``identifierName`` is created at runtime.

.. code-block:: aimms

    IsRuntimeIdentifier(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which it should be determined whether or not it is
        created at runtime.

Return Value
------------

    This function returns 0 or 1. If ``identifierName`` is not an
    identifier, an error message is issued.

.. note::

    In order to determine whether or not the value of string parameter
    ``myStr`` is an identifier, you can use
    ``StringToElement(AllIdentifiers, myStr)`` or
    ``myStr in AllIdentifiers``.

Example
-------

The code:

.. code-block:: aimms

    _bp_isRuntime := IsRuntimeIdentifier('webui_runtime::AllImplicitPublicIdentifiers');
    display _bp_isRuntime ;

produces in the listing file:

.. code-block:: aimms

    _bp_isRuntime := 1 ;

This illustrates that runtime identifiers are also used by AIMMS repository libraries including:

#.  `AIMMS WebUI <https://documentation.aimms.com/webui/index.html>`_

#.  `AIMMS DataExchange <https://documentation.aimms.com/dataexchange/index.html>`_

#.  `AIMMS Collaborative Data Management <https://documentation.aimms.com/cdm/index.html>`_.


References
-----------

    *  `Runtime Libraries and the Model Edit Functions <https://documentation.aimms.com/language-reference/advanced-language-components/model-structure-and-modules/runtime-libraries-and-the-model-edit-functions.html#runtime-libraries-and-the-model-edit-functions>`_

    *  `Retrieve Value of Dynamic <Identifier https://how-to.aimms.com/Articles/146/146-value-dynamic-identifier.html>`_ 
    
    *  `Repeat Data with Model Query and Model Edit <https://how-to.aimms.com/Articles/132/132-Repetive-Patterns-Model-Edit.html>`_

    *  The functions :aimms:func:`StringToElement`, :aimms:func:`DeclaredSubset` and :aimms:func:`IndexRange`.

    *  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    *  The common example in :numref:`CommonModelQueryExample`.
