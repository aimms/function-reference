.. aimms:procedure:: DatasetSelectNew(data\_category, dataset[, title])

.. _DatasetSelectNew:

DatasetSelectNew
================

The procedure :aimms:func:`DatasetSelectNew` shows a dialog box in which the user
can select a new dataset for a given data category.

.. code-block:: aimms

    DatasetSelectNew(
            data_category,   ! (input) element in AllDataCategories
            dataset,         ! (output) element parameter in AllDataSets
            [title]          ! (optional) string expression
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which you want to the user to select a new dataset.

    *dataset*
        An element parameter in :aimms:set:`AllDataSets`. On return the dataset will
        refer to the selected dataset.

    *title (optional)*
        A string expression that is used as the title for the dialog box. If
        this argument is omitted, then a default title is used.

Return Value
------------

    The procedure returns 1 if the user did select a dataset. If the user
    pressed **Cancel**, then the procedure returns 0.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If via this procedure the user creates a new dataset (i.e. a new
       dataset node in the data management tree), then this case dataset
       does not yet contain any data. The dataset will only contain data
       after you explicitly save data to it.

.. seealso::

    The procedures :aimms:func:`DatasetSelect`, :aimms:func:`DatasetSetCurrent`, :aimms:func:`DatasetSave`.
