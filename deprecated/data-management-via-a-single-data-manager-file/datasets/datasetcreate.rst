.. aimms:procedure:: DatasetCreate(data\_category, dataset\_path, dataset)

.. _DatasetCreate:

DatasetCreate
=============

The procedure :aimms:func:`DatasetCreate` creates a new dataset node in the Data
Management tree. The data category, the name of the dataset and the
folder in which it is created is given as an argument to the procedure.

.. code-block:: aimms

    DatasetCreate(
            data_category,     ! (input) element in AllDataCategories
            dataset_path,      ! (input) scalar string expression
            dataset            ! (output) element parameter into AllDataSets
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which a dataset must be created.

    *dataset\_path*
        A string expression holding the path and name of the new dataset. The
        path is specified relative to the corresponding data category root node
        in the Data Management tree.

    *dataset*
        An element parameter into :aimms:set:`AllDataSets`. On successful return this
        parameter will refer to the newly created element in :aimms:set:`AllDataSets`.

Return Value
------------

    The procedure returns 1 if the dataset is created successfully. It
    returns 0 if the dataset could not be created or if the dataset already
    exists.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the specified path contains folders that do not exist, then these
       folders are created automatically. To check whether a specific
       dataset path already exists you can use the procedure
       ``DatasetFind``.

.. seealso::

    The procedures :aimms:func:`DatasetFind`, :aimms:func:`DatasetDelete`.
