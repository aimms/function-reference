.. aimms:procedure:: PageGetUsedIdentifiers(page, identifier\_set)

.. _PageGetUsedIdentifiers:

PageGetUsedIdentifiers
======================

The procedure :aimms:func:`PageGetUsedIdentifiers` returns a subset of :aimms:set:`AllIdentifiers`
containing all identifiers used on a specified page.

.. code-block:: aimms

    PageGetUsedIdentifiers(
            page,            ! (input) scalar string expression
            identifier_set   ! (output) subset of all identifiers
            )

Arguments
---------

    *page*
        A string expression containing the name of a page in the Page Manager
        tree.

    *identifier\_set*
        A subset of all identifers containing all the identifiers used in the
        page.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist.

.. seealso::

    The procedure :aimms:func:`IdentifierGetUsedInformation`.
