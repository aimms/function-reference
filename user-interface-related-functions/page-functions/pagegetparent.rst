.. aimms:procedure:: PageGetParent(page, parentpage, IncludeHiddenPages)

.. _PageGetParent:

PageGetParent
=============

The procedure :aimms:func:`PageGetParent` retrieves the name of the parent page
for a specific page in the Page Manager tree.

.. code-block:: aimms

    PageGetParent(
            page,            		! (input) scalar string expression
            parentpage,       	! (output) scalar string identifier
            IncludeHiddenPages	! (optional) scalar numerical expression
            )

Arguments
---------

    *page*
        A string expression containing the name of a (child) page in the Page
        Manager tree.

    *parentpage*
        A scalar string identifier to hold the name of the parent page of the
        given page (if it exists).

    *IncludeHiddenPages*
        A scalar numerical expression to indicate whether hidden pages should be
        taken into account. If IncludeHiddenPages is set to 1 then the resulting
        parent page may be a page that is currently hidden, otherwise these
        hidden pages are skipped. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist or if the page does not have a parent page.

.. seealso::

    The procedures :aimms:func:`PageGetChild`, :aimms:func:`PageGetNext`, :aimms:func:`PageGetPrevious`, :aimms:func:`PageGetNextInTreeWalk`, :aimms:func:`PageGetAll`.
