.. aimms:procedure:: DatasetFind(data\_category, dataset\_path, dataset)

.. _DatasetFind:

DatasetFind
===========

The procedure :aimms:func:`DatasetFind` searches the Data Management tree for a
dataset with a specific name and belonging to a specific data category.

.. code-block:: aimms

    DatasetFind(
            data_category,     ! (input) element in AllDataCategories
            dataset_path,      ! (input) scalar string expression
            dataset            ! (output) element parameter into AllDataSets
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which the datasets must be searched.

    *dataset\_path*
        A string expression holding the path and name of a dataset. The path is
        specified relative to the corresponding data category root node in the
        Data Management tree.

    *dataset*
        An element parameter into :aimms:set:`AllDataSets`. On successful return this
        parameter will refer to the dataset found.

Return Value
------------

    The procedure returns 1 if the dataset is found, and 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DatasetCreate`, :aimms:func:`DatasetDelete`.
