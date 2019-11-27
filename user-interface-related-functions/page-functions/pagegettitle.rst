.. aimms:procedure:: PageGetTitle(pageName, pageTitle)

.. _PageGetTitle:

PageGetTitle
============

The procedure :aimms:func:`PageGetTitle` retrieves the title of a specific page in
the Page Manager tree.

.. code-block:: aimms

    PageGetTitle(
            pageName,      ! (input) scalar string expression
            pageTitle      ! (output) scalar string identifier
            )

Arguments
---------

    *pageName*
        A string expression containing the name of a page in the Page Manager
        tree.

    *pageTitle*
        A scalar string identifier to hold the title of the given page.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.
