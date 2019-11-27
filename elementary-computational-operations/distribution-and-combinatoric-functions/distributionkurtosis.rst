.. aimms:function:: DistributionKurtosis(distribution)

.. _DistributionKurtosis:

DistributionKurtosis
====================

The function :aimms:func:`DistributionKurtosis` computes the kurtosis of a given
distribution.

.. code-block:: aimms

    DistributionKurtosis(
               distribution             ! (input) distribution
               )

Arguments
---------

    *distribution*
        An expression representing any distribution (such as ``Normal(0,1)``).

Return Value
------------

    The function :aimms:func:`DistributionKurtosis`\ (*distribution*) returns the
    kurtosis of the given *distribution*.

.. seealso::

    You can find more information about the kurtosis of a distribution in
    Appendix A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
