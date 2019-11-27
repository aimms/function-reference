.. aimms:function:: errh::Attribute(err, loc)

.. _errh::Attribute:

errh::Attribute
===============

The function :aimms:func:`errh::Attribute` returns the identifier or node in which
the error occurred.

.. code-block:: aimms

    errh::Attribute(
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

    Returns an element in :aimms:set:`AllAttributeNames` if the information is available and the
    empty element otherwise.

.. note::

    When ``err`` does not reference an element in :aimms:set:`errh::PendingErrors` or when the
    current filter is the filter ``To Global Collector`` an additional error
    will be raised.

.. seealso::

    The functions :aimms:func:`errh::Node`, :aimms:func:`errh::Line` and :aimms:func:`errh::NumberOfLocations`.
