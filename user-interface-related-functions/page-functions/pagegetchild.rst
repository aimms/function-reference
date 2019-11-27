.. aimms:procedure:: PageGetChild(page, childpage, IncludeHiddenPages)

.. _PageGetChild:

PageGetChild
============

The procedure :aimms:func:`PageGetChild` retrieves the name of the first child
page for a specific page in the Page Manager tree.

.. code-block:: aimms

    PageGetChild(
            page,               ! (input) scalar string expression
            childpage,          ! (output) scalar string identifier
            IncludeHiddenPages  ! (optional) scalar numerical expression
            )

Arguments
---------

    *page*
        A string expression containing the name of a (parent) page in the Page
        Manager tree.

    *childpage*
        A scalar string identifier to hold the name of the first child page
        beneath the given parent page (if any).

    *IncludeHiddenPages*
        A scalar numerical expression to indicate whether hidden pages should be
        taken into account. If IncludeHiddenPages is set to 1 then the resulting
        child page may be a page that is currently hidden, otherwise these
        hidden pages are skipped. The default is 0.

Return Value
------------

    The procedure returns 1 on success, or 0 if the given page name does not
    exist or if the page does not have any child pages.

.. seealso::

    The procedures :aimms:func:`PageGetParent`, :aimms:func:`PageGetNext`, :aimms:func:`PageGetPrevious`, :aimms:func:`PageGetNextInTreeWalk`, :aimms:func:`PageGetAll`.
