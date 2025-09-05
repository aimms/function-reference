.. aimms:procedure:: me::ImportNode(esection, filename)

.. _me::ImportNode:

me::ImportNode
==============

The procedure :aimms:func:`me::ImportNode` reads a section from file.

.. code-block:: aimms

    me::ImportNode(
            esection,  ! (input) section element.
            filename)  ! (input) a string

Arguments
---------

    *esection*
        An element in the set :aimms:set:`AllIdentifiers` referencing a section in a runtime
        library.

    *filename*
        The name of file that contains a runtime library. The filename should
        have the ``.ams`` extension.

Return Value
------------

    The procedure returns 1 if the file is read successfully. If the
    procedure fails to read the file it returns 0 after raising errors.

.. seealso::

    - The functions :aimms:func:`me::CreateLibrary` and :aimms:func:`me::ExportNode`.
