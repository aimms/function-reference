.. aimms:function:: DataChangeMonitorDelete(ID)

.. _DataChangeMonitorDelete:

DataChangeMonitorDelete
=======================

With the function :aimms:func:`DataChangeMonitorDelete`, you can delete a data
change monitor that was created using the function
``DataChangeMonitorCreate``.

.. code-block:: aimms

    DataChangeMonitorDelete(
        ID                   ! (input) a scalar string expression
        )

Arguments
---------

    *ID*
        A string identifying an existing data change monitor.

Return Value
------------

    The function returns 1 upon success. If there exists no data change
    monitor for the given ``ID``, the function returns 0. In case of any
    other error, it returns :math:`-1` and ``CurrentErrorMessage`` will
    contain a proper error message.

.. seealso::

    The functions :aimms:func:`DataChangeMonitorCreate`, :aimms:func:`DataChangeMonitorReset`, :aimms:func:`DataChangeMonitorHasChanged`.
