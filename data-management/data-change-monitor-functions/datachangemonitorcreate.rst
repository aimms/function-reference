.. aimms:function:: DataChangeMonitorCreate(ID, monitoredIdentifiers[, excludeNonSaveables])

.. _DataChangeMonitorCreate:

DataChangeMonitorCreate
=======================

With the function :aimms:func:`DataChangeMonitorCreate`, you can create a new data
change monitor. With a data change monitor, you can determine whether
any identifiers in a subset of :aimms:set:`AllIdentifiers` have been changed
since the latest call to :aimms:func:`DataChangeMonitorCreate` or
``DataChangeMonitorReset``. To check for any changes, you can use
:aimms:func:`DataChangeMonitorHasChanged`.

.. code-block:: aimms

    DataChangeMonitorCreate(
        ID,                     ! (input) a scalar string expression
        monitoredIdentifiers,   ! (input) subset of AllIdentifiers 
        [excludeNonSaveables]   ! (optional) 0 or 1
        )

Arguments
---------

    *ID*
        A string identifying a (new) data change monitor.

    *monitoredIdentifiers*
        The subset of identifiers that you want to monitor for this data change
        monitor.

    *excludeNonSaveables (optional)*
        If the data change monitor is used to monitor whether or not a subset of
        identifiers needs to be saved, it is unnecessary to include identifiers
        that have the ``Nosave`` property. If you set this argument to 1, these
        identifiers will automatically be excluded from the given subset of
        identifiers. The default of this argument is 1. This exclusion is
        applied also on any subset that is passed in later calls to
        ``DataChangeMonitorReset``.

Return Value
------------

    The function returns 1 upon success. If there already exists a data
    change monitor for the given ``ID``, the function returns 0. In case of
    any other error, it returns :math:`-1`. If the return value is 0 or
    :math:`-1` ``CurrentErrorMessage`` will contain a proper error message.

.. note::

    -  The newly created monitor is reset automatically, so there is no need
       to call the function ``DataChangeMonitorReset`` immediately after
       creation.

    -  If your project uses the Data management style 'Disk files and
       folders', AIMMS itself uses a data change monitor to keep track of
       whether the active data needs to be saved before exiting, or before
       loading any new data. The ``ID`` of this internal data change monitor
       is given by the predeclared string parameter
       ``DataManagementMonitorID``.

.. seealso::

    The functions :aimms:func:`DataChangeMonitorHasChanged`, :aimms:func:`DataChangeMonitorReset`, :aimms:func:`DataChangeMonitorDelete`.
