.. aimms:function:: Poisson(lambda)

.. _Poisson:

Poisson
=======

The function :aimms:func:`Poisson` draws a random value from a Poisson
distribution.

.. code-block:: aimms

    Poisson(
        AverageNumberOfSuccesses     ! (input) numerical expression
        )

Arguments
---------

    *lambda*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Poisson` returns a random value drawn from a Poisson
    distribution with average number of occurrences
    *AverageNumberOfSuccesses*.

.. seealso::

    The :aimms:func:`Poisson` distribution is discussed in full detail in Appendix A
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
