.. aimms:procedure:: OpenDocument(document)

.. _OpenDocument:

OpenDocument
============

The procedure :aimms:func:`OpenDocument` uses the current association of Windows
to open documents, run programs, etc. Its procedureality is similar to
that of the **Run** command in the **Start Menu** of Windows. You can
use it, for instance, to display an HTML file using the default web
browser, open a Word document, or initiate an e-mail session.

.. code-block:: aimms

    OpenDocument(
            document          ! (input) string expression
            )

Arguments
---------

    *document*
        A string expression representing the document or program you want to
        open.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

Example
-------

    .. code-block:: aimms

            OpenDocument( "http://www.aimms.com" );
            OpenDocument( "mailto:info@aimms.com" );
            OpenDocument( "anyfile.doc" );
            OpenDocument( "c:\\windows" );

.. seealso::

    The procedure :aimms:func:`Execute`.
