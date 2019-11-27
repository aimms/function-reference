.. aimms:procedure:: PageSetCursor(page, tag, scalar\_reference)

.. _PageSetCursor:

PageSetCursor
=============

With the procedure :aimms:func:`PageSetCursor` you have maximum control over where
you want to set the current keyboard input focus. Similar to
``PageSetFocus`` you can specify which page object should get the focus,
but additionally you can specify the data element that should be
highlighted within the focus object.

.. code-block:: aimms

    PageSetCursor(
            page              ! (input) scalar string expression
            tag,              ! (input) scalar string expression
            scalar_reference, ! (input) scalar identifier
            )

Arguments
---------

    *page*
        A string expression representing the name of the page in which you want
        to set the input focus.

    *tag*
        A string expression representing the tag name of the object that should
        get the keyboard input focus.

    *scalar\_reference*
        A scalar data element that matches the element that you want to
        highlight within the object.

Return Value
------------

    The procedure returns 1 on success. If it fails, then it returns 0 and
    the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

Example
-------

    If you are displaying a variable ``Transport`` in a table with tag
    "TransportTable" on page "Results", then you can set the focus and
    cursor to a specific cell in this table using the following procedure
    call: 

    .. code-block:: aimms

                PageSetCursor("Results", "TransportTable", Transport('Amsterdam','Rotterdam'));

.. note::

    You can specify a unique tag name for each page object via the object
    properties.

.. seealso::

    The procedure :aimms:func:`PageSetFocus`.
