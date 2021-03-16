.. aimms:procedure:: CaseTypeCategories(case\_type, category\_set)

.. _CaseTypeCategories:

CaseTypeCategories
==================

The procedure :aimms:func:`CaseTypeCategories` retrieves the sub-collection of
data categories that is included in a specific case type.

.. code-block:: aimms

    CaseTypeCategories(
            case_type,         ! (input) element of the set AllCaseTypes
            category_set       ! (output) subset of AllDataCategories
            )

Arguments
---------

    *case\_type*
        An element of the set :aimms:set:`AllCaseTypes`, refering to the case type for
        which you want to retrieve the included data categories.

    *category\_set*
        A subset of the set :aimms:set:`AllDataCategories`, on successfull return this
        subset is filled with the data categories included in the case type.

Return Value
------------

    The procedure returns 1 on success, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`CaseGetType`, :aimms:func:`CaseTypeContents`, :aimms:func:`DataCategoryContents`.
