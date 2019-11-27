.. aimms:function:: errh::Severity(err)

.. _errh::Severity:

errh::Severity
==============

The function :aimms:func:`errh::Severity` returns the severity of the error.

.. code-block:: aimms

    errh::Severity(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns an element in :aimms:set:`errh::AllErrorSeverities` if the information is available and the
    empty element otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The procedures :aimms:func:`errh::Adapt` and :aimms:func:`errh::MarkAsHandled`.
