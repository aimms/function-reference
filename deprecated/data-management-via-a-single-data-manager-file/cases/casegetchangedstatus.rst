.. aimms:function:: CaseGetChangedStatus(None)

.. _CaseGetChangedStatus:

CaseGetChangedStatus
====================

The function :aimms:func:`CaseGetChangedStatus` returns whether the data of the
currently active case has changed and thus needs to be saved.

.. code-block:: aimms

    CaseGetChangedStatus

Arguments
---------

    *None*

Return Value
------------

    The function returns 1 if the data has changed, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`DataChangeMonitorHasChanged`
       instead.

.. seealso::

    The functions :aimms:func:`CaseSetChangedStatus`, :aimms:func:`CaseSave`.
