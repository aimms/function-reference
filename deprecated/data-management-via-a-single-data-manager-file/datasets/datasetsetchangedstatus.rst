.. aimms:procedure:: DatasetSetChangedStatus(data\_category, status)

.. _DatasetSetChangedStatus:

DatasetSetChangedStatus
=======================

The procedure :aimms:func:`DatasetSetChangedStatus` can set the status of a data
category to either changed or unchanged.

.. code-block:: aimms

    DatasetSetChangedStatus(
            data_category,    ! (input) element in AllDataCategories
            status            ! (input) 0 or 1
            )

Arguments
---------

    *data\_category*
        An element in ``AllDataCategories``, specifying the data category for
        which you want to set the changed status.

    *status*
        An integer value holding the new dataset status: 0 for unchanged, 1 for
        changed.

Return Value
------------

    The procedure returns 1.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The function :aimms:func:`DatasetGetChangedStatus`.
