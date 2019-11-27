.. aimms:function:: DistributionDensity(distribution, x)

.. _DistributionDensity:

DistributionDensity
===================

The function :aimms:func:`DistributionDensity` computes the density of a given
distribution.

.. code-block:: aimms

    DistributionDensity(
               distribution,            ! (input) distribution
               x                        ! (input) numerical expression
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`DistributionDensity`\ (*distribution*,\ :math:`x`), for
    :math:`x\in(-\infty,\infty)` returns the expected density around
    :math:`x` of sample points from *distribution*. It is the derivative of
    ``DistributionCumulative(distr,x)``.

.. seealso::

    The functions :aimms:func:`DistributionCumulative`, :aimms:func:`DistributionInverseDensity`. The function :aimms:func:`DistributionDensity`
    is discussed in full detail in Appendix A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
