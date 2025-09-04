.. aimms:function:: SectionIdentifiers(SectionName)

.. _SectionIdentifiers:

SectionIdentifiers
==================

The function :aimms:func:`SectionIdentifiers` determines which identifiers are
declared within a specific section in the model tree.

.. code-block:: aimms

    SectionIdentifiers(
         SectionName       ! (input) scalar element parameter
         )

Arguments
---------

    *SectionName*
        An element expression in the set :aimms:set:`AllSections` specifying the section for
        which the identifiers should be listed.

Return Value
------------

    This function returns a subset of :aimms:set:`AllIdentifiers` containing all the
    identifiers that are declared within the specified section, excluding
    the section itself and its prefix (if the section is a module or
    library). When ``SectionName`` is the empty element, the empty set is
    returned.

Example
-------

Given the declarations:

.. code-block:: aimms

    Parameter p1;
    Parameter p2;
    Parameter pd {
        Definition: p1 + p2;
    }

The following code collects all identifiers referenced in a section, includining the procedure.

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

    _ep_sec := StringToElement(AllIdentifiers,
        "chapterModel::sectionModelQuery::Function_SectionIdentifiers",
        create:0);
    _s_refIds := SectionIdentifiers(_ep_sec);
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _s_refIds ;
    endblock ;

produces in the listing file:

.. code-block:: aimms

    _s_refIds := data 
    { 'chapterModel::sectionModelQuery::funcSectionIdentifiers::pr_testSectionIdentifiers',
      'chapterModel::sectionModelQuery::funcSectionIdentifiers::p1'                       ,
      'chapterModel::sectionModelQuery::funcSectionIdentifiers::p2'                       ,
      'chapterModel::sectionModelQuery::funcSectionIdentifiers::pd'                       } ;

References
-----------

   -  `Working with the Set AllIdentifiers <https://documentation.aimms.com/language-reference/data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers.html#working-with-the-set-allidentifiers>`_.

