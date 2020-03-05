.. aimms:procedure:: HistogramGetFrequencies(histogram\_id, frequencies)

.. _HistogramGetFrequencies:

HistogramGetFrequencies
=======================

Through the procedure :aimms:func:`HistogramGetFrequencies` you can obtain the
observed frequencies for each interval in a histogram.

.. code-block:: aimms

    HistogramGetFrequencies(
         histogram_id,         ! (input) a scalar number
         frequencies           ! (output) a one-dimensional parameter
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` procedure.

    *frequencies*
        A one-dimensional identifier that will be filled with the frequencies of
        each interval in the histogram. The cardinality of the domain set should
        be at least the number of intervals.

Return Value
------------

    The procedure returns 1 if the frequencies are retrieved successfully,
    or 0 otherwise.

.. seealso::

    The procedures :aimms:func:`HistogramCreate`, :aimms:func:`HistogramAddObservation`, :aimms:func:`HistogramAddObservations`. Histogram support in
    AIMMS is discussed in full detail in Section A.6 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
