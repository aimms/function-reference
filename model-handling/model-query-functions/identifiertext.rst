.. aimms:function:: IdentifierText(identifierName)

.. _IdentifierText:

IdentifierText
==============

The function :aimms:func:`IdentifierText` returns the string representation of the text attribute of ``identifierName``
or, if the text is not specified, the name of the identifier.

.. code-block:: aimms

    IdentifierText(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the text should be obtained.

Return Value
------------

    This function returns a string containing the text attribute of ``identifierName``.
    If ``identifierName`` is not an identifier, an error message is issued. 
    When the text is not specified, the name of the identifier is returned.

.. note::

    This function replaces the deprecated suffix :ref:`.txt`.

.. seealso::

    -  The functions :aimms:func:`IdentifierText`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The common example in :numref:`CommonModelQueryExample`.
