.. aimms:procedure:: me::ExportNode(esection, filename)

.. _me::ExportNode:

me::ExportNode
==============

The procedure :aimms:func:`me::ExportNode` writes a section to file.

.. code-block:: aimms

    me::ExportNode(
            esection,  ! (input) section element.
            filename)  ! (input) a string

Arguments
---------

    *esection*
        An element in the set :aimms:set:`AllIdentifiers` referencing a runtime library or a
        section in a runtime library.

    *filename*
        The name of file to which the section is written. The filename should
        have the ``.ams`` extension.

Return Value
------------

    The procedure returns 1 if the file is written successfully. If the
    procedure fails to write the file it returns 0 after raising errors.

.. seealso::

    The functions :aimms:func:`me::CreateLibrary`, :aimms:func:`me::ImportLibrary` and :aimms:func:`me::ImportNode`.
