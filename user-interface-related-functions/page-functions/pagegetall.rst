.. aimms:procedure:: PageGetAll(page\_set, IncludePages, IncludeTemplates, ExcludeHidden, ExcludePrintables)

.. _PageGetAll:

PageGetAll
==========

With the procedure :aimms:func:`PageGetAll` you can retrieve the names of all
pages and/or templates in your project

.. code-block:: aimms

    PageGetAll(
            page_set,           ! (output) an (empty) root set
            IncludePages,       ! (optional, default 1) scalar expression
            IncludeTemplates,   ! (optional, default 1) scalar expression 
            ExcludeHidden,      ! (optional, default 0) scalar expression
            ExcludePrintables   ! (optional, default 0) scalar expression        
            )

Arguments
---------

    *page\_set*
        A root set, that on return will contain the names of all the requested
        pages.

    *IncludePages*
        A scalar numerical expression to indicate whether the returned set
        should contain the names of pages in your project.

    *IncludeTemplates*
        A scalar numerical expression to indicate whether the returned set
        should contain the names of templates in your project.

    *ExcludeHidden*
        A scalar numerical expression to indicate whether hidden pages should be
        part of the returned set. If ExcludeHidden is set to 1 then the returned
        set will not contain any page that is currenlty hidden.

    *ExcludePrintables*
        A scalar numerical expression to indicate whether print pages or print
        templates should be part of the returned set. Print pages/templates are
        those pages/templates that are especially created for printing (i.e. in
        the Template Manager they are placed as children of a root print
        template). If ExcludePrintables is set to 1 then the returned set will
        not contain any printable page or template.

Return Value
------------

    The procedure returns 1 on success, and 0 on failure.

.. seealso::

    The procedures :aimms:func:`PageGetNext`, :aimms:func:`PageGetPrevious`, :aimms:func:`PageGetChild`, :aimms:func:`PageGetParent`, :aimms:func:`PageGetNextInTreeWalk`.
