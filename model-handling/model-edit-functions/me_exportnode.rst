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


Example
-------

Viewing a small runtime library with prefix ``frerl`` in the model explorer:

.. figure:: images/runtimelib-setup.png
    :align: center

|

Let ``ep_functionReferenceExampleRuntimeLib`` be the element parameter 
that holds the root of that library as value, then the code:

.. code-block:: aimms

    me::ExportNode(
        esection :  ep_functionReferenceExampleRuntimeLib, 
        filename :  "test.ams");

writes the contents of the runtime library to the file ``test.ams``.

.. seealso::

    - :aimms:func:`me::CreateLibrary`.
    - :aimms:func:`me::ImportLibrary`.
    - :aimms:func:`me::ImportNode`.
	- :aimms:func:`me::ExportNode` plays an essential role in `Create a static AIMMS Library from a runtime library <https://how-to.aimms.com/Articles/581/581-static-lib-from-runtime-lib.html>`_.
    - Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_.
