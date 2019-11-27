.. aimms:procedure:: PageSetFocus(page, tag)

.. _PageSetFocus:

PageSetFocus
============

With the procedure :aimms:func:`PageSetFocus` you can set the keyboard input focus
to a specific object within a specific page. If the page is not open,
then the procedure will first try to open the page.

.. code-block:: aimms

    PageSetFocus(
                page,       ! (input) scalar string expression
                tag         ! (input) scalar string expression
                )

Arguments
---------

    *page*
        A string expression representing the name of the page in which you want
        to set the input focus.

    *tag*
        A string expression representing the tag name of the object that should
        get the keyboard input focus.

Return Value
------------

    The procedure returns 1 on success. If it fails to set the focus to the
    specified object, then the return value is 0 and :aimms:set:`CurrentErrorMessage` will contain
    a proper error message.

.. note::

    You can specify a unique tag name for each page object via the object
    properties.

.. seealso::

    The procedures :aimms:func:`PageSetCursor`, :aimms:func:`PageGetFocus`.
