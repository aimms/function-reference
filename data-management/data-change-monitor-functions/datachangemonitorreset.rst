.. aimms:function:: DataChangeMonitorReset(ID, monitoredIdentifiers)

.. _DataChangeMonitorReset:

DataChangeMonitorReset
======================

The function :aimms:func:`DataChangeMonitorReset` assigns a new set of identifiers
to an existing data change monitor and resets the monitor to the
'unchanged' status.

.. code-block:: aimms

    DataChangeMonitorReset(
        ID,                     ! (input) a scalar string expression
        monitoredIdentifiers    ! (input) subset of AllIdentifiers 
        )

Arguments
---------

    *ID*
        A string identifying an existing data change monitor.

    *monitoredIdentifiers*
        The subset of identifiers that should be monitored by the data change
        monitor.

Return Value
------------

    The function returns 1 upon success. If there exists no data change
    monitor for the given ``ID``, the function returns 0. In case of any
    other error it returns :math:`-1` and ``CurrentErrorMessage`` will
    contain a proper error message.

.. seealso::

    - The functions :aimms:func:`DataChangeMonitorCreate`, :aimms:func:`DataChangeMonitorHasChanged`, :aimms:func:`DataChangeMonitorDelete`.
