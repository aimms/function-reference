.. aimms:procedure:: DatasetSave(data\_category[, confirm])

.. _DatasetSave:

DatasetSave
===========

The procedure :aimms:func:`DatasetSave` saves the data of a data category to the
active dataset. If there is no named active dataset, then the procedure
behaves exactly as the ``DatasetSaveAs`` procedure.

.. code-block:: aimms

    DatasetSave(
            data_category,   ! (input) element in AllDataCategories
            [confirm]        ! (optional) 0, 1 or 2
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which you want to save the data.

    *confirm (optional)*
        An integer to indicate whether or not the procedure should ask for
        confirmation before overwriting the existing dataset. If 0, then no
        confirmation dialog box is shown. If 1 (default), then whether or not
        the confirmation dialog box is shown depends on the case type
        properties. If 2, then always a confirmation dialog box is shown.

Return Value
------------

    The procedure returns 1 if the dataset is saved successfully. It returns
    0 if the user canceled the save operation. If any other error occurs,
    then the procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain an
    error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DatasetSaveAs`, :aimms:func:`DatasetSaveAll`, :aimms:func:`DatasetLoadCurrent` and function :aimms:func:`DatasetGetChangedStatus`.
