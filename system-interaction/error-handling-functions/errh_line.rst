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


Example
-------

.. code-block:: aimms
    :linenos:

    block 
        pr_divideByZero();
    onerror _ep_err do
        _p_line := errh::Line(_ep_err);
        errh::MarkAsHandled( _ep_err, 1 );
    endblock ;

Afterwards:

.. code-block:: aimms

    _p_line = 2

.. seealso::

    The function :aimms:func:`errh::Column`, :aimms:func:`errh::Filename`, :aimms:func:`errh::Attribute`, :aimms:func:`errh::Node` and :aimms:func:`errh::NumberOfLocations`.
