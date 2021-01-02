.. aimms:procedure:: HistogramAddObservation(histogram\_id, value)

.. _HistogramAddObservation:

HistogramAddObservation
=======================

The procedure :aimms:func:`HistogramAddObservation` adds a new observation to a
histogram that was previously created through the procedure
``HistogramCreate``.

.. code-block:: aimms

    HistogramAddObservation(
         histogram_id,         ! (input) a scalar parameter
         value                 ! (input) a scalar value
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` procedure.

    *value*
        The value of a new observation that should be added to the histogram.

Return Value
------------

    The procedure returns 1 if the new observation is added successfully, or
    0 otherwise.

.. seealso::

    The procedure :aimms:func:`HistogramAddObservations`, :aimms:func:`HistogramCreate`. Histogram support in AIMMS is
    discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
