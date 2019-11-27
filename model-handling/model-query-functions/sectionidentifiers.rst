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
