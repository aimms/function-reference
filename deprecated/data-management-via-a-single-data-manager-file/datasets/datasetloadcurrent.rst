.. aimms:procedure:: DatasetLoadCurrent(data\_category, dataset[, dialog])

.. _DatasetLoadCurrent:

DatasetLoadCurrent
==================

The procedure :aimms:func:`DatasetLoadCurrent` loads an existing dataset as the
new current dataset for a specific data category. You can use it to load
either a dataset that is passed as argument to the procedure, or a
dataset that the user can select via a dialog box. If the data of the
corresponding data category has changed, then the user is asked to save
this data first.

.. code-block:: aimms

    DatasetLoadCurrent(
           data_category, ! (input) element in AllDataCategories
           dataset,       ! (input/output) an element parameter into AllDataSets
           [dialog]       ! (optional) 0 or 1
           )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which a dataset is loaded.

    *dataset*
        An element parameter in the set ``AllDataSets``. If the argument
        *dialog* is set to 0, then no dialog box is shown and the dataset to
        which the element parameter currently refers is loaded. If the argument
        *dialog* is set to 1, then the value of the element parameter is used to
        initialize the dialog box. The dataset that the user has selected and is
        loaded successfully is returned through this argument.

    *dialog (optional)*
        An integer value indicating whether or not the user gets a dialog box in
        which he can select the dataset to load. The default value is 1, thus if
        this argument is omitted the dialog box will be shown.

Return Value
------------

    The procedure returns 1 on success. If the user canceled the operation,
    then the procedure returns 0. If any other error occurs then the
    procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If you want to suppress the dialog box for the unsaved data, then you
       may call ``DatasetSetChangedStatus(category,0)`` prior to
       :aimms:func:`DatasetLoadCurrent`.

.. seealso::

    The procedures :aimms:func:`DatasetLoadIntoCurrent`, :aimms:func:`DatasetMerge`, :aimms:func:`DatasetSave`, :aimms:func:`DatasetSetChangedStatus`.
