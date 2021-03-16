.. aimms:procedure:: CaseTypeContents(case\_type, identifier\_set)

.. _CaseTypeContents:

CaseTypeContents
================

The procedure :aimms:func:`CaseTypeContents` retrieves the sub-collection of
identifiers that is contained in a specific case type.

.. code-block:: aimms

    CaseTypeContents(
            case_type,           ! (input) element of the set AllCaseTypes
            identifier_set       ! (output) subset of AllIdentifiers
            )

Arguments
---------

    *case\_type*
        An element of the set :aimms:set:`AllCaseTypes`, refering to the case type for
        which you want to retrieve the contents.

    *identifier\_set*
        A subset of the set :aimms:set:`AllIdentifiers`, on successful return this subset is
        filled with all identifiers contained in the case type.

Return Value
------------

    The procedure returns 1 on success, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  The procedure returns the contents of the case type itself, as well
       as the contents of all data categories that are included in the case
       type.

.. seealso::

    The procedures :aimms:func:`CaseGetType`, :aimms:func:`CaseTypeCategories`, :aimms:func:`DataCategoryContents`.
