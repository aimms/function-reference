.. aimms:function:: IdentifierType(identifierName)

.. _IdentifierType:

IdentifierType
==============

The function :aimms:func:`IdentifierType` returns the type of ``identifierName``
as an element in :aimms:set:`AllIdentifierTypes`.

.. code-block:: aimms

    IdentifierType(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the type should be obtained.

Return Value
------------

    This function returns a type as an element in :aimms:set:`AllIdentifierTypes`. If
    ``identifierName`` is not an identifier, an error message is issued.

.. note::

    This function replaces the suffix :ref:`.type`; this suffix is deprecated.

.. seealso::

    -  The functions :aimms:func:`IdentifierDimension` and :aimms:func:`IdentifierUnit`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The common example in :numref:`CommonModelQueryExample`.
