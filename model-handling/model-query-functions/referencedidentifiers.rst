.. aimms:function:: ReferencedIdentifiers(searchIdentSet, searchAttrSet, recursive)

.. _ReferencedIdentifiers:

ReferencedIdentifiers
=====================

The function :aimms:func:`ReferencedIdentifiers` determines which identifiers are
used in the specified attributes of a subset of :aimms:set:`AllIdentifiers`.

.. code-block:: aimms

    ReferencedIdentifiers(
         searchIdentSet       ! (input) subset of AllIdentifiers
         searchAttrSet        ! (input) subset of AllAttributeNames
         recursive            ! (optional) numerical expression
         )

Arguments
---------

    *searchIdentSet*
        The set of identifiers to search in for referenced identifiers. This is
        a subsetof :aimms:set:`AllIdentifiers`.

    *searchAttrSet*
        The set of attributes to search in for referenced identifiers. This is a
        subset of :aimms:set:`AllAttributeNames`.

    *recursive*
        Optional argument, default 0, if 1 this function will also search in the
        referenced identifiers for identifier references.

Return Value
------------

    This function returns a subset of :aimms:set:`AllIdentifiers` containing all the
    identifiers that are referenced in the attributes in *searchAttrSet* in
    one of the identifiers in *searchIdentSet*.

.. seealso::

    The function :aimms:func:`ConstraintVariables` and :aimms:func:`VariableConstraints`
