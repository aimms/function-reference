.. aimms:procedure:: DatasetGetCategory(dataset, data\_category)

.. _DatasetGetCategory:

DatasetGetCategory
==================

The procedure :aimms:func:`DatasetGetCategory` retrieves the data category of a
specific dataset.

.. code-block:: aimms

    DatasetGetCategory(
            dataset,        ! (input) element of the set AllDataSets
            data_category   ! (output) element parameter into AllDataCategories
            )

Arguments
---------

    *dataset*
        An element of the set :aimms:set:`AllDataSets`, refering to the dataset for which
        you want to retrieve its data category.

    *data\_category*
        An element parameter into :aimms:set:`AllDataCategories`, on successfull return
        this argument will contain the data category of the given dataset.

Return Value
------------

    The procedure returns 1 on success, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.
