.. aimms:function:: DataChangeMonitorHasChanged(ID)

.. _DataChangeMonitorHasChanged:

DataChangeMonitorHasChanged
===========================

The function :aimms:func:`DataChangeMonitorHasChanged` returns whether the data of
any identifier that is monitored by the specified data change monitor
has been changed since a previous call to ``DataChangeMonitorCreate`` or
``DataChangeMonitorReset``.

.. code-block:: aimms

    DataChangeMonitorHasChanged(
        ID                   ! (input) a scalar string expression
        )

Arguments
---------

    *ID*
        A string identifying an existing data change monitor.

Return Value
------------

    The function returns 1 if any of the identifiers monitored by the data
    change monitor has been changed since a previous call to either
    ``DataChangeMonitorCreate`` or ``DataChangeMonitorReset``. If none of
    the identifiers has been changed, the function returns 0. In case of any
    other error, it returns :math:`-1` and ``CurrentErrorMessage`` will
    contain a proper error message. If the monitored set contains
    identifiers that were not present in that set at the previous call to
    either ``DataChangeMonitorCreate`` or ``DataChangeMonitorReset``, these
    identifiers are assumed to be changed, and the function returns 1 as
    well.

    .. note::

        -  Calling :aimms:func:`DataChangeMonitorHasChanged` does not reset the data change monitor.

.. seealso::

    - The functions :aimms:func:`DataChangeMonitorCreate`, :aimms:func:`DataChangeMonitorReset`, :aimms:func:`DataChangeMonitorDelete`.
