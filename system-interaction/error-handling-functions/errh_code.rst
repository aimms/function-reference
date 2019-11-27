.. aimms:function:: errh::Code(err)

.. _errh::Code:

errh::Code
==========

The function :aimms:func:`errh::Code` returns the identification code of the
format string.

.. code-block:: aimms

    errh::Code(
            err  ! (input) an element
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

Return Value
------------

    Returns an element in :aimms:set:`errh::ErrorCodes` if the information is available and the
    empty element otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The function :aimms:func:`errh::Category` and the procedure :aimms:func:`errh::Adapt`. The predeclared
    identifier :aimms:set:`errh::PendingErrors`.
