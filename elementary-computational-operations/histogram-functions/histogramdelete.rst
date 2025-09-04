.. aimms:procedure:: HistogramDelete(histogram_id)

.. _HistogramDelete:

HistogramDelete
===============

The procedure :aimms:func:`HistogramDelete` deletes a histogram that was created
using the ``HistogramCreate`` procedure. After the historgram has been
deleted, the histogram id is no longer valid.

.. code-block:: aimms

    HistogramDelete(
         histogram_id         ! (input) a scalar parameter
         )

Arguments
---------

    *histogram\_id*
        A scalar value representing a histogram that was previously created
        using the ``HistogramCreate`` procedure. When the procedure returns,
        this *histogram_id* no longer refers to a valid histogram.

Return Value
------------

    The procedure returns 1 if the histogram is deleted successfully, or 0
    otherwise.

.. seealso::

    - The procedure :aimms:func:`HistogramCreate`. 
    - Histogram support in AIMMS is discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/creating-histograms` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
