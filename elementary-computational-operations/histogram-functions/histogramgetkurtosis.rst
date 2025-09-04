.. aimms:function:: HistogramGetKurtosis(histogram_id)

.. _HistogramGetKurtosis:

HistogramGetKurtosis
====================

The function :aimms:func:`HistogramGetKurtosis` returns the kurtosis coefficient
of all observations in a histogram.

.. code-block:: aimms

    HistogramGetKurtosis(
         histogram_id         ! (input) a scalar number
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` function.

Return Value
------------

    The function returns the kurtosis coefficient of all observations in the
    histogram.

.. seealso::

    - The functions :aimms:func:`HistogramCreate`, :aimms:func:`HistogramGetObservationCount`, :aimms:func:`HistogramGetAverage`, :aimms:func:`HistogramGetDeviation`, :aimms:func:`HistogramGetSkewness`.
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
