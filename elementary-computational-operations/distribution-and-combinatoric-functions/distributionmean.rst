.. aimms:function:: DistributionMean(distribution)

.. _DistributionMean:

DistributionMean
================

The function :aimms:func:`DistributionMean` computes the mean of a given
distribution.

.. code-block:: aimms

    DistributionMean(
               distribution             ! (input) distribution
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

Return Value
------------

    The function :aimms:func:`DistributionMean`\ (*distribution*) returns the mean of
    the given *distribution*.

.. seealso::

    You can find more information about the mean of a distribution in
    :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
