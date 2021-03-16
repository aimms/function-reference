.. aimms:function:: CaseGetDatasetReference(case, data-category, dataset)

.. _CaseGetDatasetReference:

CaseGetDatasetReference
=======================

With the function :aimms:func:`CaseGetDatasetReference` you can, for every data
category, obtain a reference to the dataset that is included in a
specific case.

.. code-block:: aimms

    CaseGetDatasetReference(
            case,             ! (input) element from the set AllCases
            data_category,    ! (input) element from the set AllDataCategories
            dataset           ! (output) element parameter into AllDataSets
            )

Arguments
---------

    *case*
        An element in the set :aimms:set:`AllCases`, refering to the case for which you
        want to retrieve the dataset reference.

    *data-category*
        An element in the set :aimms:set:`AllDataCategories`, refering to the specific
        data category for which you want to obtain the dataset reference.

    *dataset*
        An element parameter into :aimms:set:`AllDataSets`, on return this argument will
        contain the included dataset. It is set to the empty element if no
        dataset is included or if the dataset no longer exists.

Return Value
------------

    If any of the first two arguments does not refer to a valid case or data
    category, or if the data category is not part of the case type, then the
    function returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message. If a dataset is included, and this dataset still exists, then
    the function returns 1 and the argument *dataset* will refer to that
    dataset. If there is no dataset included, then the function returns 1
    and *dataset* is set to the empty element. If a dataset is included, but
    this dataset has been deleted, then the function returns 0 and *dataset*
    is set to the empty element.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  You can use the functions ``CaseGetType`` and ``CaseTypeCategories``
       to check whether a specific data category is part of a case.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders`` there is no valid replacement.

.. seealso::

    The functions :aimms:func:`CaseGetType`, :aimms:func:`CaseTypeCategories`.
