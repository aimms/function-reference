.. aimms:procedure:: HistogramSetDomain(histogram_id, intervals[, left, width, left_tail, right_tail])

.. _HistogramSetDomain:

HistogramSetDomain
==================

With the procedure :aimms:func:`HistogramSetDomain` you can override the default
layout of frequency intervals of a histogram.

.. code-block:: aimms

    HistogramSetDomain(
         histogram_id,       ! (input) a scalar number
         intervals,          ! (input) a positive integer number
         [left,]             ! (optional) a scalar expression
         [width,]            ! (optional) a positive scalar number
         [left_tail,]        ! (optional) 0 or 1
         [right_tail]        ! (optional) 0 or 1
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` procedure.

    *intervals*
        The number of fixed-width intervals (not including the *left\_* or
        *right_tail* interval).

    *left (optional)*
        The lower bound of the left-most interval (not including the left-tail
        interval). If omitted, then the histogram will use the observations to
        determine this bound.

    *width (optional)*
        The (fixed) width of each interval. If omitted, then the histogram will
        use the observations to determine the width.

    *left\_tail (optional)*
        An indicator whether or not a left-tail interval should be created. If
        this argument is omitted, then the default value of 1 is used (creating
        a left-tail interval).

    *right\_tail (optional)*
        An indicator whether or not a right-tail interval should be created. If
        this argument is omitted, then the default value of 1 is used (creating
        a right-tail interval).

Return Value
------------

    The procedure returns 1 if the domain is changed successfully, or 0
    otherwise.

.. seealso::

    - The procedures :aimms:func:`HistogramCreate`, :aimms:func:`HistogramGetBounds`. 
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
