.. aimms:procedure:: PageGetFocus(page, tag[, fullPathTag])

.. _PageGetFocus:

PageGetFocus
============

With the procedure :aimms:func:`PageGetFocus` you can retrieve the name of the
currently active page.

.. code-block:: aimms

    PageGetFocus(
            page,            ! (output) scalar string identifier
            tag,             ! (output) scalar string identifier
            [fullPathTag]    ! (optional) 0 or 1
            )

Arguments
---------

    *page*
        A string identifier to hold the name of the currently active page. If
        the same page name is used in more than one (library) project, then the
        prefix of the library project (or ``::`` in case of the main project)
        will be prepended.

    *tag*
        A string identifier to hold the tag name of the object that currently
        has the keyboard input focus.

    *fullPathTag (optional)*
        If this value is set to 0, then returned tag will be the simple tag name
        of the object that has focus. If this value is set to 1 (the default),
        then the returned tag name will also contain the tags of Tabbed or
        Indexed Page objects in which the object with focus is contained. See
        the remarks below.

Return Value
------------

    The procedure returns 1 on success, or 0 if there is no currently active
    page or if no object has the input focus.

.. note::

    You can specify a unique tag name for each page object via the object
    properties. If no tag name has been given explicitly, then the type of
    object is returned ("Table", "Bar Chart", etc.) If an object with tag
    "X" is displayed in a tabbed page object with tag "T", then the full
    path tag name will be "T::X". If an object with tag "X" is displayed in
    an indexed page object with tag "IP" on a row and column that
    corresponds with elements "rowi" and "colj", then the full path tag name
    will be "IP('rowi','colj')::X".

.. seealso::

    The procedures :aimms:func:`PageSetFocus`, :aimms:func:`PageGetActive`.
