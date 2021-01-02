.. aimms:function:: NegativeBinomial(ProbabilityOfSuccess, NumberOfSuccesses)

.. _NegativeBinomial:

NegativeBinomial
================

The function :aimms:func:`NegativeBinomial` draws a random value from a negative
binomial distribution.

.. code-block:: aimms

    NegativeBinomial(
        ProbabilityOfSuccess,   ! (input) numerical expression
        NumberOfSuccesses       ! (input) integer expression
        )

Arguments
---------

    *ProbabilityOfSuccess*
        A scalar numerical expression in the range :math:`(0,1)`.

    *NumberOfSuccesses*
        A integer numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`NegativeBinomial` returns a random value drawn from a
    negative binomial distribution with probability *ProbabilityOfSuccess*
    and number of successes *NumberOfSuccesses*.

.. seealso::

    The :aimms:func:`NegativeBinomial` distribution is discussed in full detail in
    :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
