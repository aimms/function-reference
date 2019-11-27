.. aimms:function:: errh::NumberOfLocations(err)

.. _errh::NumberOfLocations:

errh::NumberOfLocations
=======================

The function :aimms:func:`errh::NumberOfLocations` returns the number of locations
stored to which this error is relevant. The relevant locations are file
(if any) that is being read, and the procedures currently active.

.. code-block:: aimms

    errh::NumberOfLocations(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns the number locations for which this error is relevant.

.. note::

    When ``err`` doesn't reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The functions :aimms:func:`errh::Node`, :aimms:func:`errh::Attribute` and :aimms:func:`errh::Line`.
