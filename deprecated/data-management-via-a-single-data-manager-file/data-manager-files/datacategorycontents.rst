.. aimms:procedure:: DataCategoryContents(data\_category, identifier\_set)

.. _DataCategoryContents:

DataCategoryContents
====================

The procedure :aimms:func:`DataCategoryContents` retrieves the sub-collection of
identifiers that is contained in a specific data category.

.. code-block:: aimms

    DataCategoryContents(
            data_category,       ! (input) element of the set AllDataCategories
            identifier_set       ! (output) subset of AllIdentifiers
            )

Arguments
---------

    *data\_category*
        An element of the set ``AllDataCategories``, refering to the data
        category for which you want to retrieve the contents.

    *identifier\_set*
        A subset of the set :aimms:set:`AllIdentifiers`, on successful return this subset is
        filled with all identifiers contained in the data category.

Return Value
------------

    The procedure returns 1 on success, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`CaseTypeCategories`, :aimms:func:`CaseTypeContents`.
