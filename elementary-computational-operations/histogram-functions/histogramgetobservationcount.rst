.. aimms:function:: HistogramGetObservationCount(histogram\_id)

.. _HistogramGetObservationCount:

HistogramGetObservationCount
============================

The function :aimms:func:`HistogramGetObservationCount` returns the total number
of observations in a histogram.

.. code-block:: aimms

    HistogramGetObservationCount(
         histogram_id         ! (input) a scalar number
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` function.

Return Value
------------

    The function returns the total number of observations in a histogram.

.. seealso::

    The functions :aimms:func:`HistogramCreate`, :aimms:func:`HistogramGetAverage`, :aimms:func:`HistogramGetDeviation`, :aimms:func:`HistogramGetSkewness`, :aimms:func:`HistogramGetKurtosis`.
    Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of
    the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
