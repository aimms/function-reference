.. aimms:function:: DistributionCumulative(distribution, x)

.. _DistributionCumulative:

DistributionCumulative
======================

The function :aimms:func:`DistributionCumulative` computes the cumulative
probability value of a given distribution.

.. code-block:: aimms

    DistributionCumulative(
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

    The function ``CumulativeDistribution``\ (*distribution*,\ :math:`x`),
    for :math:`x\in(-\infty,\infty)` returns the probability
    :math:`P(X\leq x)` where the stochastic variable :math:`X` is
    distributed according to the given *distribution*.

.. note::

    For continuous distributions AIMMS can compute the derivatives of the
    cumulative and inverse cumulative distribution functions. As a
    consequence, you may use these functions in the constraints of a
    nonlinear model when the second argument is a variable.

.. seealso::

    The function :aimms:func:`DistributionInverseCumulative`. The function :aimms:func:`DistributionCumulative` is
    discussed in full detail in Appendix A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
