.. aimms:procedure:: PageClose([page])

.. _PageClose:

PageClose
=========

With the procedure :aimms:func:`PageClose` you can close a page that is currently
open.

.. code-block:: aimms

    PageClose(
            page             ! (optional) string expression
            )

Arguments
---------

    *page (optional)*
        A string expression representing the name of the page that you want to
        close. This name is the unique name as it appears in the Page Manager
        tree. If you omit this argument, then :aimms:func:`PageClose` closes the currently
        active page.

Return Value
------------

    The procedure returns 1 if the page is closed successfully, or a 0
    otherwise.

.. note::

    The active page can be obtained by :aimms:func:`PageGetActive`.

.. seealso::

    The procedures :aimms:func:`PageOpen`, :aimms:func:`PageGetActive`, and :aimms:func:`PageOpenSingle`.
