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

Example
-------

Given the declarations:

.. code-block:: aimms

    Parameter p1;
    Parameter p2;
    Parameter pd {
        Definition: p1 + P2;
    }

The following code, checks the definition of ``pd`` to determine that the 
identifiers ``p1`` and ``p2`` are referenced.

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 5-8

    _ep_pd := StringToElement(AllIdentifiers,
        "chapterModel::sectionModelQuery::funcReferencedIdentifiers::pd",
        create:0);
    _s_ids += _ep_pd ;
    _s_refIds := ReferencedIdentifiers(
        searchIdentSet :  _s_ids, 
        searchAttrSet  :  AllAttributeNames, 
        recursive      :  1);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _s_refIds ;
    endblock ;

produces in the listing file:

.. code-block:: aimms

    _s_refIds := data 
    { 'chapterModel::sectionModelQuery::funcReferencedIdentifiers::p1',
      'chapterModel::sectionModelQuery::funcReferencedIdentifiers::p2' } ;


References
-----------

    -   :aimms:func:`ConstraintVariables`. 

    -   :aimms:func:`VariableConstraints`.

    -   `ReferencedIdentifiers <https://how-to.aimms.com/Articles/582/582-reduce-client-server-exchange.html>`_.

    -   `Working with the Set AllIdentifiers <https://documentation.aimms.com/language-reference/data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers.html#working-with-the-set-allidentifiers>`_.
