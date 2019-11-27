.. aimms:function:: errh::Line(err, loc)

.. _errh::Line:

errh::Line
==========

The function :aimms:func:`errh::Line` returns the line number in the file or
attribute in which the error occured.

.. code-block:: aimms

    errh::Line(
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

    Returns a line number if the information is available and 0 otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The function :aimms:func:`errh::Column`, :aimms:func:`errh::Filename`, :aimms:func:`errh::Attribute`, :aimms:func:`errh::Node` and :aimms:func:`errh::NumberOfLocations`.
