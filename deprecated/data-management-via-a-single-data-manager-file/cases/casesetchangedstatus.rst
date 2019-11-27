.. aimms:procedure:: CaseSetChangedStatus(status[, include\_datasets])

.. _CaseSetChangedStatus:

CaseSetChangedStatus
====================

The procedure :aimms:func:`CaseSetChangedStatus` can set the status of the current
case to either changed or unchanged.

.. code-block:: aimms

    CaseSetChangedStatus(
            status,               ! (input) 0 or 1
            [include_datasets]    ! (optional) 0 or 1
            )

Arguments
---------

    *status*
        An integer value holding the new case status: 0 for unchanged, 1 for
        changed.

    *include\_datasets (optional)*
        An integer to indicate whether or not the the status of the included and
        active datasets should be set as well. If you omit this argument, then
        the default value is 0 (status of datasets is not set).

Return Value
------------

    The procedure returns 1.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`DataChangeMonitorCreate` or
       :aimms:func:` DataChangeMonitorReset` instead.

.. seealso::

    The procedures :aimms:func:`CaseGetChangedStatus`, :aimms:func:`DatasetSetChangedStatus`.
