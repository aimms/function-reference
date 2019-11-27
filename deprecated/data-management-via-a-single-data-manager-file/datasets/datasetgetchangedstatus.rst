.. aimms:function:: DatasetGetChangedStatus(data\_category)

.. _DatasetGetChangedStatus:

DatasetGetChangedStatus
=======================

The function :aimms:func:`DatasetGetChangedStatus` returns whether the data
associated with a specific data category has changed and thus needs to
be saved.

.. code-block:: aimms

    DatasetGetChangedStatus(
            data_category         ! (input) element in AllDataCategories
            )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which the changed status must be retrieved.

Return Value
------------

    The function returns 1 if the data has changed, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The functions :aimms:func:`DatasetSetChangedStatus`, :aimms:func:`DatasetSave`.
