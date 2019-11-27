.. aimms:function:: DistributionInverseCumulative(distribution, alpha)

.. _DistributionInverseCumulative:

DistributionInverseCumulative
=============================

The function :aimms:func:`DistributionInverseCumulative` computes the inverse
cumulative probability value of a given distribution.

.. code-block:: aimms

    DistributionInverseCumulative(
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
    :aimms:func:`DistributionInverseCumulative`\ (*distribution*,\ :math:`\alpha`),
    for :math:`\alpha\in[0,1]` computes the largest
    :math:`x\in(-\infty,\infty)` such that the probability
    :math:`P(X\leq x)\leq\alpha` where the stochastic variable :math:`X` is
    distributed according to the given *distribution*.

.. note::

    For continuous distributions AIMMS can compute the derivatives of the
    cumulative and inverse cumulative distribution functions. As a
    consequence, you may use these functions in the constraints of a
    nonlinear model when the second argument is a variable.

.. seealso::

    The function :aimms:func:`DistributionCumulative`. The function :aimms:func:`DistributionInverseCumulative`
    is discussed in full detail in Appendix A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
