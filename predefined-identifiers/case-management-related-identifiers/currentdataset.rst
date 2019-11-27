.. aimms:set:: CurrentDataSet

.. _CurrentDataSet:

CurrentDataSet
==============

The predefined element parameter :aimms:set:`CurrentDataSet` contains a reference
to the current actively loaded dataset(s) within an AIMMS project.

.. code-block:: aimms

        ElementParameter CurrentDataSet {
            IndexDomain  :  IndexDataCategories;
            Range        :  AllDataSets;
        }

Definition
----------

    The element parameter :aimms:set:`CurrentDataSet` contains, for every data
    category, an (integer) dataset reference (as an element of :aimms:set:`AllDataSets`) to
    the current actively loaded dataset within the active case, or is empty
    if there no named dataset loaded as active for a particular data
    category.

Updatability
------------

    The value of the element parameter :aimms:set:`CurrentDataSet` can only be
    modified by actively actively loading datasets into the active case
    either in the **Data Manager**, through the **Data** menu, or using the
    functions :aimms:func:`DatasetLoadCurrent` and :aimms:func:`DatasetSaveAs`.

.. note::

    This identifier is only relevant when the chosen
    ``Data_Management_style`` is ``single_data_manager_file``.
