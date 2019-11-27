.. aimms:function:: Exponential(lowerbound, scale)

.. _Exponential:

Exponential
===========

The function :aimms:func:`Exponential` draws a random value from an exponential
distribution.

.. code-block:: aimms

    Exponential(
          lowerbound      ! (optional) numerical expression
          scale           ! (optional) numerical expression
         )

Arguments
---------

    *lowerbound*
        A scalar numerical expression.

    *scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Exponential` returns a random value drawn from a
    exponential distribution with lower bound *lowerbound* and scale
    *scale*.

.. note::

    The prototype of this function has changed with the introduction of
    AIMMS 3.4. In order to run models that still use the original prototype,
    the option ``Distribution_compatibility`` should be set to
    ``Aimms_3_0``. The original function :aimms:func:`Exponential`\ (*lambda*) returns
    a random value drawn from a exponential distribution with rate
    :math:`lambda = 1/scale` and lower bound :math:`0`.

.. seealso::

    The :aimms:func:`Exponential` distribution is discussed in full detail in Appendix
    A of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
