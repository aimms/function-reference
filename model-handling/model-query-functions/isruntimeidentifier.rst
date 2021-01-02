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

.. seealso::

    -  The functions :aimms:func:`StringToElement`, :aimms:func:`DeclaredSubset` and :aimms:func:`IndexRange`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The common example in :numref:`CommonModelQueryExample`.
