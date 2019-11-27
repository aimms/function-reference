.. aimms:function:: Binomial(ProbabilityOfSuccess, NumberOfTries)

.. _Binomial:

Binomial
========

The function :aimms:func:`Binomial` draws a random value from a binomial
distribution.

.. code-block:: aimms

    Binomial(
            ProbabilityOfSuccess, ! (input) numerical expression
            NumberOfTries         ! (input) integer expression
            )

Arguments
---------

    *ProbabilityOfSuccess*
        A scalar numerical expression in range :math:`(0,1)`.

    *NumberOfTries*
        An integer numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Binomial` returns a random value drawn from a binomial
    distribution with a probability of success *ProbabilityOfSuccess* and
    number of tries *NumberOfTries*

.. seealso::

    The :aimms:func:`Binomial` distribution is discussed in full detail in Appendix A
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
