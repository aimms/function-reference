.. aimms:procedure:: PageOpenSingle(page)

.. _PageOpenSingle:

PageOpenSingle
==============

The procedure :aimms:func:`PageOpenSingle` is similar to ``PageOpen``, except that
after successfull opening the page :aimms:func:`PageOpenSingle` makes sure that
all other currently opened pages are closed.

.. code-block:: aimms

    PageOpenSingle(
                  page        ! (input) string expression
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

    The procedures :aimms:func:`PageOpen`, :aimms:func:`PageClose`.
