.. aimms:procedure:: PageGetPrevious(page, previouspage, IncludeHiddenPages)

.. _PageGetPrevious:

PageGetPrevious
===============

The procedure :aimms:func:`PageGetPrevious` retrieves the name of the previous
page for a specific page in the Page Manager tree. The previous page is
the page that has the same parent page, and is positioned directly above
the given page.

.. code-block:: aimms

    PageGetPrevious(
            page,            		! (input) scalar string expression
            previouspage,     	! (output) scalar string identifier
            IncludeHiddenPages	! (optional) scalar numerical expression
            )

Arguments
---------

    *page*
        A string expression containing the name of a (child) page in the Page
        Manager tree.

    *previouspage*
        A scalar string identifier to hold the name of the previous page of the
        given page (if it exists).

    *IncludeHiddenPages*
        A scalar numerical expression to indicate whether hidden pages should be
        taken into account. If IncludeHiddenPages is set to 1 then the resulting
        page may be a page that is currently hidden, otherwise these hidden
        pages are skipped. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist or if the page does not have a previous page.

.. seealso::

    The procedures :aimms:func:`PageGetNext`, :aimms:func:`PageGetChild`, :aimms:func:`PageGetParent`, :aimms:func:`PageGetNextInTreeWalk`, :aimms:func:`PageGetAll`.
