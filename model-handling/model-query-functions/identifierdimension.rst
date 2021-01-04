.. aimms:function:: IdentifierDimension(identifierName)

.. _IdentifierDimension:

IdentifierDimension
===================

The function :aimms:func:`IdentifierDimension` returns the data dimension of
``identifierName``.

.. code-block:: aimms

    IdentifierDimension(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the dimension should be obtained.

Return Value
------------

    This function returns a non-negative integer. If ``identifierName`` is
    not an identifier, an error message is issued. If ``identifierName`` is
    not an indexed parameter, variable or constraint, a 0 is returned
    without further warning.

.. note::

    This function replaces the deprecated suffix :ref:`.dim`.

.. seealso::

    -  The functions :aimms:func:`DomainIndex` and :aimms:func:`IndexRange`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The common example in :numref:`CommonModelQueryExample`.
