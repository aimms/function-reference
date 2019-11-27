.. aimms:procedure:: DatasetSaveAs(data\_category, dataset)

.. _DatasetSaveAs:

DatasetSaveAs
=============

The procedure :aimms:func:`DatasetSaveAs` shows a dialog box in which the user can
specify a (new) dataset to which the data is saved.

.. code-block:: aimms

    DatasetSaveAs(
           data_category,   ! (input) element in AllDataCategories
           dataset          ! (output) element parameter in AllDataSets
           )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which you want to save the data.

    *dataset*
        An element parameter in ``AllDataSets``. On return this parameter will
        refer to the dataset that the user selected.

Return Value
------------

    The procedure returns 1 if the dataset is saved successfully. It returns
    0 if the user cancelled the save operation. If any other error occurs,
    then the procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain an
    error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DatasetSave`, :aimms:func:`DatasetSaveAll`, :aimms:func:`DatasetLoadCurrent`, :aimms:func:`DatasetGetChangedStatus`.
