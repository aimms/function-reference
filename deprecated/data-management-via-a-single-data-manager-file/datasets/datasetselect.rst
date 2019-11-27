.. aimms:procedure:: DatasetSelect(data\_category, dataset[, title])

.. _DatasetSelect:

DatasetSelect
=============

The procedure :aimms:func:`DatasetSelect` shows a dialog box in which the user can
select an existing dataset for a given data category.

.. code-block:: aimms

    DatasetSelect(
            data_category,   ! (input) element in AllDataCategories
            dataset,         ! (output) element parameter in AllDataSets
            [title]          ! (optional) string expression
            )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which you want to the user to select a dataset.

    *dataset*
        An element parameter in ``AllDataSets``. On return the dataset will
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

.. seealso::

    The procedure :aimms:func:`DatasetSelectNew`.
