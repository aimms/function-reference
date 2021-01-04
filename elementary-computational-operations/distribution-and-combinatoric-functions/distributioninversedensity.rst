.. aimms:function:: DistributionInverseDensity(distribution, alpha)

.. _DistributionInverseDensity:

DistributionInverseDensity
==========================

The function :aimms:func:`DistributionInverseDensity` computes the density of the
inverse cumulative function of a given distribution.

.. code-block:: aimms

    DistributionInverseDensity(
               distribution,            ! (input) distribution
               alpha                    ! (input) numerical expression
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

    *alpha*
        A scalar numerical expression within the interval :math:`[0,1]`.

Return Value
------------

    The function
    :aimms:func:`DistributionInverseDensity`\ (*distribution*,\ :math:`\alpha`), for
    :math:`\alpha\in[0,1]` returns the inverse density from *distribution*.
    It is the derivative of ``DistributionInverseCumulative(distr,alpha)``.

.. seealso::

    The function :aimms:func:`DistributionDensity`. The function :aimms:func:`DistributionInverseDensity` is
    discussed in full detail in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
