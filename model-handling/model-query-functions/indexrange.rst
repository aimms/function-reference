.. aimms:function:: IndexRange(indexName)

.. _IndexRange:

IndexRange
==========

The function :aimms:func:`IndexRange` returns the range of an index as an element
in :aimms:set:`AllIdentifiers`.

.. code-block:: aimms

    IndexRange(
         indexName       ! (input) scalar element parameter
         )

Arguments
---------

    *indexName*
        An element expression in the predefined set ``AllIdentifiers``
        specifying the index for which the range should be returned.

Return Value
------------

    This function returns the range of index ``indexName`` as an element in
    :aimms:set:`AllIdentifiers`. If ``indexName`` is not an index or if it does not have a
    range the empty element is returned.

Example
-------

    With the declarations 

    .. code-block:: aimms

                Set MasterSet {
                    Index      :  a;
                }
                Index b {
                    Range      :  MasterSet;
                }
                Index c;

    The output of the statements

    .. code-block:: aimms

                put "IndexRange( 'a' ) = \"", IndexRange( 'a' ):10, "\"", / ;
                put "IndexRange( 'b' ) = \"", IndexRange( 'b' ):10, "\"", / ;
                put "IndexRange( 'c' ) = \"", IndexRange( 'c' ):10, "\"", / ;

    is: 

    .. code-block:: aimms

                IndexRange( 'a' ) = "MasterSet "
                IndexRange( 'b' ) = "MasterSet "
                IndexRange( 'c' ) = "          "

.. seealso::

    The functions :aimms:func:`DeclaredSubset` and :aimms:func:`DomainIndex`.
