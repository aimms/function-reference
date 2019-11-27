.. aimms:procedure:: PageGetNextInTreeWalk(page, nextpage, IncludeHiddenPages)

.. _PageGetNextInTreeWalk:

PageGetNextInTreeWalk
=====================

The procedure :aimms:func:`PageGetNextInTreeWalk` retrieves the name of the next
page for a specific page in the Page Manager tree by traversing the tree
in a depth-first manner: This procedure will try to find the next page
of a page first by searching for child nodes of the selected page. If
the page has no child nodes, it will look for a next page on the same
level. If there also isn't a next page in the same level, it will try to
find a next page for the parent nodes. This procedure includes hidden
pages and ignores separators.

.. code-block:: aimms

    PageGetNextInTreeWalk(
            page,           ! (input) scalar string expression
            nextpage,        ! (output) scalar string identifier
           IncludeHiddenPages	! (optional) scalar numerical expression
            )

Arguments
---------

    *page*
        A string expression containing the name of a (child) page in the Page
        Manager tree.

    *nextpage*
        A scalar string identifier to hold the name of the next page of the
        given page (if it exists).

    *IncludeHiddenPages*
        A scalar numerical expression to indicate whether hidden pages should be
        taken into account. If IncludeHiddenPages is set to 1 then the resulting
        parent page may be a page that is currently hidden, otherwise these
        hidden pages are skipped. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist or if the page does not have a next page.

.. seealso::

    The procedures :aimms:func:`PageGetNext`, :aimms:func:`PageGetPrevious`, :aimms:func:`PageGetChild`, :aimms:func:`PageGetParent`, :aimms:func:`PageGetAll`.
