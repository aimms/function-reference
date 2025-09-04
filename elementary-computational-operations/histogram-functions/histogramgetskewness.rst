.. aimms:function:: HistogramGetSkewness(histogram_id)

.. _HistogramGetSkewness:

HistogramGetSkewness
====================

The function :aimms:func:`HistogramGetSkewness` returns the skewness of all
observations in a histogram.

.. code-block:: aimms

    HistogramGetSkewness(
         histogram_id         ! (input) a scalar number
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` function.

Return Value
------------

    The function returns the skewness of all observations in the histogram.

.. seealso::

    - The functions :aimms:func:`HistogramCreate`, :aimms:func:`HistogramGetObservationCount`, :aimms:func:`HistogramGetAverage`, :aimms:func:`HistogramGetDeviation`, :aimms:func:`HistogramGetKurtosis`.
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
