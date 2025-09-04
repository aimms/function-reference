.. aimms:function:: DistributionDeviation(distribution)

.. _DistributionDeviation:

DistributionDeviation
=====================

The function :aimms:func:`DistributionDeviation` computes the expected deviation
of the given distribution .

.. code-block:: aimms

    DistributionDeviation(
               distribution             ! (input) distribution
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

Return Value
------------

    The function :aimms:func:`DistributionDeviation`\ (*distribution*) returns the
    expected deviation (distance from the mean) of the *distribution*.

.. seealso::

    - You can find more information about the deviation of a distribution in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
