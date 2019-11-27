.. aimms:function:: DomainIndex(identifierName, indexPosition)

.. _DomainIndex:

DomainIndex
===========

The function :aimms:func:`DomainIndex` returns the ``indexPosition``-th index of
``identifierName`` as an element in :aimms:set:`AllIdentifiers`.

.. code-block:: aimms

    DomainIndex(
         identifierName,       ! (input) scalar element parameter
         indexPosition
         )        ! (input) scalar integer parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which an index should be obtained.

    *indexPosition*
        An expression in the range :math:`\{1..dim\}` where :math:`dim` is the
        dimension of ``identifierName``.

Return Value
------------

    This function returns an element in the set :aimms:set:`AllIdentifiers` representing the
    ``indexPosition`` index of ``identifierName``. If ``identifierName`` is
    not an indexed parameter, variable or constraint, or if
    ``indexPosition`` is outside the range :math:`\{1..dim\}`, the empty
    element is returned without further warning.

Example
-------

    The following code uses the function :aimms:func:`DomainIndex` to obtain the
    indices of the index domain of a parameter: 

    .. code-block:: aimms

                put outf ;
                for ( IndexParameters | IdentifierDimension( IndexParameters ) > 0 ) do
                   put IndexParameters:0, "(" ;
                   while loopcount <= IdentifierDimension( IndexParameters ) do
                       put DomainIndex( IndexParameters, loopcount ):0 ;
                       if loopCount < IdentifierDimension( IndexParameters ) then put "," ; endif ;
                   endwhile ;
                   put ")", /  ; 
                endfor ;
                putclose ;

    A fragment of
    the output of this code might look as follows: 

    .. code-block:: aimms

                LowFP(f,p)
                UppFP(f,p)
                Supply(c)
                Demand(f)

.. seealso::

    The functions :aimms:func:`IdentifierDimension`, :aimms:func:`DeclaredSubset` and :aimms:func:`IndexRange`.
