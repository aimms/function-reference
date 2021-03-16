.. aimms:procedure:: DatasetDelete(data\_category, dataset)

.. _DatasetDelete:

DatasetDelete
=============

The procedure :aimms:func:`DatasetDelete` deletes a specific dataset node from the
Data Management tree.

.. code-block:: aimms

    DatasetDelete(
            data_category,   ! (input) element in AllDataCategories
            dataset          ! (input) element parameter into AllDataSets
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which a dataset is be deleted.

    *dataset*
        An element parameter into :aimms:set:`AllDataSets`, representing the dataset that
        you want to delete.

Return Value
------------

    The procedure returns 1 if the dataset is deleted successfully, or 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedure :aimms:func:`DatasetFind`.
