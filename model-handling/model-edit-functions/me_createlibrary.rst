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


Example
-------

The code

.. code-block:: aimms

	ep_functionReferenceExampleRuntimeLib := me::CreateLibrary(
		libraryName :  sp_functionReferenceExampleLibName, 
		prefixName  :  sp_functionReferenceExampleLibPrefix );
	_ep_type := IdentifierType(ep_functionReferenceExampleRuntimeLib);
	display _ep_type ;

creates a runtime library, and produces in the listing file:

.. code-block:: aimms

    _ep_type := 'LibraryModule' ;

.. seealso::

    - :aimms:func:`me::ImportLibrary`. 
	- :aimms:func:`me::Create`.
    - Generic references for model edit functions can be found on the `index page <https://documentation.aimms.com/functionreference/model-handling/model-edit-functions/index.html>`_.