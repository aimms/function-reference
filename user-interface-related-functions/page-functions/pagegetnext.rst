.. aimms:procedure:: PageGetNext(page, nextpage, IncludeHiddenPages)

.. _PageGetNext:

PageGetNext
===========

The procedure :aimms:func:`PageGetNext` retrieves the name of the next page for a
specific page in the Page Manager tree. The next page is the page that
has the same parent page, and is positioned directly below the given
page.

.. code-block:: aimms

    PageGetNext(
            page,           		! (input) scalar string expression
            nextpage,        		! (output) scalar string identifier
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
        page may be a page that is currently hidden, otherwise these hidden
        pages are skipped. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist or if the page does not have a next page.

.. seealso::

    The procedures :aimms:func:`PageGetPrevious`, :aimms:func:`PageGetChild`, :aimms:func:`PageGetParent`, :aimms:func:`PageGetNextInTreeWalk`, :aimms:func:`PageGetAll`.
