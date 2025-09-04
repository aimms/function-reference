.. aimms:function:: HistogramCreate(histogram_id[, integer_histogram][, sample_buffer_size])

.. _HistogramCreate:

HistogramCreate
===============

The function :aimms:func:`HistogramCreate` sets up a new histogram. The created
histogram does not yet contain any observations. These observations must
be added later using the function ``HistogramAddObservation`` or
``HistogramAddObservations``.

.. code-block:: aimms

    HistogramCreate(
         histogram_id,           ! (output) a scalar parameter
         [integer_histogram,]    ! (optional) 0 or 1
         [sample_buffer_size]    ! (optional) a positive integer value
         )

Arguments
---------

    *histogram\_id*
        On return, this argument will contain a unique identification number,
        that is used to refer to the created histogram in other functions.

    *integer\_histogram (optional)*
        A logical indicator that specifies whether the observations will be
        integer-valued. Default is 0 (not integer).

    *sample\_buffer\_size (optional)*
        The sample buffer size used in the histogram. If omitted, a default
        buffer size of 512 is used.

Return Value
------------

    The function returns 1 if the histogram is created successfully, or 0
    otherwise.

.. seealso::

    - The functions :aimms:func:`HistogramDelete`, :aimms:func:`HistogramAddObservation`, :aimms:func:`HistogramAddObservations`. 
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
