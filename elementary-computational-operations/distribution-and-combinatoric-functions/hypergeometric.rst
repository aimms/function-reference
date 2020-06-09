.. aimms:function:: HyperGeometric(ProbabilityOfSuccess, NumberOfTries, PopulationSize)

.. _HyperGeometric:

HyperGeometric
==============

The function :aimms:func:`HyperGeometric` draws a random value from a
hypergeometric distribution.

.. code-block:: aimms

    HyperGeometric(
        ProbabilityOfSuccess,   ! (input) numerical expression
        NumberOfTries,          ! (input) integer expression
        PopulationSize          ! (input) integer expression
                  )

Arguments
---------

    *ProbabilityOfSuccess*
        A scalar numerical expression in the range :math:`(0,1)`.

    *NumberOfTries*
        A integer numerical expression in the range
        :math:`1,\dots,{PopulationSize}`.

    *PopulationSize*
        A integer numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`HyperGeometric` returns a random value drawn from a
    hypergeometric distribution with a probability of success
    *ProbabilityOfSuccess*, number of tries *NumberOfTries* and population
    size *PopulationSize*.

.. note::

    The probability of success *ProbabilityOfSuccess* must assume one of the
    values :math:`i/{size}`, where :math:`i` is in the range
    :math:`1,\dots,{PopulationSize}-1`.

.. seealso::

    The :aimms:func:`HyperGeometric` distribution is discussed in full detail in
    Appendix A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
