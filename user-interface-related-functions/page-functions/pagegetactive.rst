.. aimms:procedure:: PageGetActive(page)

.. _PageGetActive:

PageGetActive
=============

With the procedure :aimms:func:`PageGetActive` you can retrieve the name of the
currently active page.

.. code-block:: aimms

    PageGetActive(
            page             ! (output) scalar string identifier
            )

Arguments
---------

    *page*
        A string identifier to hold the name of the page that is currently
        active. If the same page name is used in more than one (library)
        project, then the prefix of the library project (or ``::`` in case of
        the main project) will be prepended.

Return Value
------------

    The procedure returns 1 on success, or 0 if there is no currently active
    page.

.. seealso::

    The procedures :aimms:func:`PageGetFocus` and :aimms:func:`PageClose`.
