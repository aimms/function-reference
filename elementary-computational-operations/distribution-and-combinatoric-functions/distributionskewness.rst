.. aimms:function:: DistributionSkewness(distribution)

.. _DistributionSkewness:

DistributionSkewness
====================

The function :aimms:func:`DistributionSkewness` computes the skewness of a given
distribution.

.. code-block:: aimms

    DistributionSkewness(
               distribution             ! (input) distribution
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

Return Value
------------

    The function :aimms:func:`DistributionSkewness`\ (*distribution*) returns the
    skewness of the given *distribution*.

.. seealso::

    - You can find more information about the skewness of a distribution in :doc:`appendices/distributions-statistical-operators-and-histogram-functions/discrete-distributions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`_.
