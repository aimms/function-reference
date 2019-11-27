.. aimms:function:: errh::MarkAsHandled(err, actually)

.. _errh::MarkAsHandled:

errh::MarkAsHandled
===================

The procedure :aimms:func:`errh::MarkAsHandled` marks or unmarks an error as
handled.

.. code-block:: aimms

    errh::MarkAsHandled(
            err,     ! (input) an element
            actually ! (optional input), default 1.
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

    *actually*
        When 1, the error ``err`` is marked as handled, when 0, the mark is
        cleared.

Return Value
------------

    Returns a line number if the information is available and 0 otherwise.

.. note::

    When ``err`` doesn't reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The function :aimms:func:`errh::IsMarkedAsHandled`.
