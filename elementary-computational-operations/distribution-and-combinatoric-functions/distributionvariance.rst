.. aimms:function:: DistributionVariance(distribution)

.. _DistributionVariance:

DistributionVariance
====================

The function :aimms:func:`DistributionVariance` computes the variance of a given
distribution.

.. code-block:: aimms

    DistributionVariance(
               distribution             ! (input) distribution
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

Return Value
------------

    The function :aimms:func:`DistributionVariance`\ (*distribution*) returns the
    variance of the given *distribution*.

.. seealso::

    - You can find more information about the variance of a distribution in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
