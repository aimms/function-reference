.. aimms:function:: me::CreateLibrary(libraryName, prefixName)

.. _me::CreateLibrary:

me::CreateLibrary
=================

The function :aimms:func:`me::CreateLibrary` creates a new runtime library.

.. code-block:: aimms

    me::CreateLibrary(
            libraryName,   ! (input) a string
            prefixName     ! (optional) a string
    )

Arguments
---------

    *libraryName*
        The name of the new runtime library.

    *prefixName*
        The name of the new prefix, when not specified one is generated from the
        ``libraryName``.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllIdentifiers` referencing the
    library when successful and the empty element upon failure. In the
    latter case at least one error has been raised.

.. seealso::

    -  The functions :aimms:func:`me::ImportLibrary` and :aimms:func:`me::Create`.

    -  The AIMMS blog post: `Getting value of a dynamic
       identifier <http://blog.aimms.com/2011/11/getting-value-of-a-dynamic-identifier/>`__
       illustrates the use of model edit functions.
