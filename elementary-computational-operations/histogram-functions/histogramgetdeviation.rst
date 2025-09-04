.. aimms:function:: HistogramGetDeviation(histogram_id)

.. _HistogramGetDeviation:

HistogramGetDeviation
=====================

The function :aimms:func:`HistogramGetDeviation` returns the standard deviation of
all observations in a histogram.

.. code-block:: aimms

    HistogramGetDeviation(
         histogram_id         ! (input) a scalar number
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` function.

Return Value
------------

    The function returns the standard deviation of all observations in the
    histogram.

.. seealso::

    - The functions :aimms:func:`HistogramCreate`, :aimms:func:`HistogramGetObservationCount`, :aimms:func:`HistogramGetAverage`, :aimms:func:`HistogramGetSkewness`, :aimms:func:`HistogramGetKurtosis`.
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
