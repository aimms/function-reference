.. aimms:function:: HistogramGetBounds(histogram\_id, left\_bound, right\_bound)

.. _HistogramGetBounds:

HistogramGetBounds
==================

Through the function :aimms:func:`HistogramGetBounds` you can obtain the lower and
upper bounds of frequency interval in a histogram.

.. code-block:: aimms

    HistogramGetBounds(
         histogram_id,         ! (input) a scalar number
         left_bound,           ! (output) a one-dimensional parameter
         right_bound           ! (output) a one-dimensional parameter
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` function.

    *left\_bound*
        A one-dimensional identifier that will be filled with the left bound of
        each interval in the histogram. The cardinality of the domain set should
        be at least the number of intervals.

    *right\_bound*
        A one-dimensional identifier that will be filled with the right bound of
        each interval in the histogram. The cardinality of the domain set should
        be at least the number of intervals.

Return Value
------------

    The function returns 1 if the bounds are retrieved successfully, or 0
    otherwise.

.. seealso::

    The functions :aimms:func:`HistogramCreate`, :aimms:func:`HistogramSetDomain`. Histogram support in AIMMS is
    discussed in full detail in Section A.6 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
