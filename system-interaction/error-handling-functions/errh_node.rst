.. aimms:function:: errh::Node(err, loc)

.. _errh::Node:

errh::Node
==========

The function :aimms:func:`errh::Node` returns the identifier or node in which the
error occurred.

.. code-block:: aimms

    errh::Node(
            err,  ! (input) an element
            loc   ! (optional input) an integer, default 1.
    )

Arguments
---------

    *err*
        An element in the set :aimms:set:`errh::PendingErrors` referencing an error.

    *loc*
        An integer in the range ``{ 1 .. errh::NumberOfLocations(err) }``.

Return Value
------------

    Returns an element in :aimms:set:`AllSymbols` if the information is available and the
    empty element otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The functions :aimms:func:`errh::Attribute`, :aimms:func:`errh::Line` and :aimms:func:`errh::NumberOfLocations`.
