.. aimms:function:: me::Create(name, newType, parentId, pos)

.. _me::Create:

me::Create
==========

The function :aimms:func:`me::Create` creates a runtime identifier.

.. code-block:: aimms

    me::Create(
            name,     ! (input) a string
            newType,  ! (input) an element
            parentId, ! (input) an element
            pos       ! (optional) an integer
    )

Arguments
---------

    *name*
        A string that is valid name for a runtime identifier.

    *newType*
        An element in the set :aimms:set:`AllIdentifierTypes`.

    *parentId*
        An element in the set :aimms:set:`AllSymbols` referencing a runtime identifier.

    *pos*
        1 is the first position, and 0 means "place at end", the default is 0.

Return Value
------------

    Returns an element in :aimms:set:`AllSymbols` if successful or the empty element
    otherwise. In the latter case error(s) have been raised. When
    ``runtimeId`` doesn't reference a runtime identifier an error will be
    raised.

.. seealso::

    -  The functions :aimms:func:`me::Delete` and :aimms:func:`me::SetAttribute`.

    -  :doc:`Articles/146/146-value-dynamic-identifier`
       illustrates the use of model edit functions. The purpose of
       :aimms:func:`me::Create` in that post is to create the procedure that does the
       actual retrieving of the data.
