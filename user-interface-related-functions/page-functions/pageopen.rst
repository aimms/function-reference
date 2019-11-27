.. aimms:procedure:: PageOpen(page)

.. _PageOpen:

PageOpen
========

With the procedure :aimms:func:`PageOpen` you can open any page that is defined in
the Page Manager. If the page is already open, then the procedure will
make this page the active page. The :aimms:func:`PageOpen` procedure does not halt
the execution, unless the page to open is defined as a dialog page. In
the latter case, the execution is halted until the user closes the page.

.. code-block:: aimms

    PageOpen(
            page             ! (input) string expression
            )

Arguments
---------

    *page*
        A string expression representing the name of the page that you want to
        open. This name is the unique name as it appears in the Page Manager
        tree.

Return Value
------------

    The procedure returns 1 if the page is opened successfully. If the
    procedure fails to open the page it returns 0, and the pre-defined
    parameter :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. seealso::

    The procedures :aimms:func:`PageOpenSingle`, :aimms:func:`PageClose`.
