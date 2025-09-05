.. aimms:function:: me::ImportLibrary(filename)

.. _me::ImportLibrary:

me::ImportLibrary
=================

The function :aimms:func:`me::ImportLibrary` reads a runtime library from an
``.ams`` file.

.. code-block:: aimms

    me::ImportLibrary(
            filename)   ! (input) a string

Arguments
---------

    *filename*
        The name of file that contains a runtime library.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllIdentifiers` referencing the
    library when successful and the empty element upon failure. In the
    latter case at least one error has been raised.

.. seealso::

    - The functions :aimms:func:`me::CreateLibrary`, :aimms:func:`me::ImportNode` and :aimms:func:`me::ExportNode`.
