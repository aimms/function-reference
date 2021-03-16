.. aimms:procedure:: DatasetSetCurrent(data\_category, dataset)

.. _DatasetSetCurrent:

DatasetSetCurrent
=================

The procedure :aimms:func:`DatasetSetCurrent` sets the dataset that is regarded as
the current dataset for a given data category. It does not load or save
any data or checks whether data needs to be saved. You can, for example,
use it to make a newly created dataset the current dataset, so that
during a DatasetSave the data is written to this dataset.

.. code-block:: aimms

    DatasetSetCurrent(
            data_category,    ! (input) element in AllDataCategories
            dataset           ! (input) element of the set AllDataSets
            )

Arguments
---------

    *data\_category*
        An element in :aimms:set:`AllDataCategories`, specifying the data category for
        which you want to set the current dataset.

    *dataset*
        An element of the set :aimms:set:`AllDataSets`, refering to the dataset that
        should become the current dataset.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DatasetNew`, :aimms:func:`DatasetCreate`, :aimms:func:`DatasetSelectNew`, :aimms:func:`DatasetSave`.
