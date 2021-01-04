.. aimms:procedure:: HistogramAddObservations(histogram\_id, values)

.. _HistogramAddObservations:

HistogramAddObservations
========================

The procedure :aimms:func:`HistogramAddObservations` adds a set of observations to
a histogram that was previously created through the procedure
``HistogramCreate``.

.. code-block:: aimms

    HistogramAddObservations(
         histogram_id,         ! (input) a scalar parameter
         values                ! (input) a one-dimensional parameter
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` procedure.

    *values*
        A one-dimensional identifier that contains the values of new
        observations that should be added to the histogram. The cardinality
        should be at least 1.

Return Value
------------

    The procedure returns 1 if the new observation is added successfully, or
    0 otherwise.

.. seealso::

    The procedure :aimms:func:`HistogramAddObservation`, :aimms:func:`HistogramCreate`. Histogram support in AIMMS is
    discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
