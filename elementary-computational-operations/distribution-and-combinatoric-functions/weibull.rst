.. aimms:function:: Weibull(Shape, Lowerbound, Scale)

.. _Weibull:

Weibull
=======

The function :aimms:func:`Weibull` draws a random value from a Weibull
distribution.

.. code-block:: aimms

    Weibull(
           Shape,       ! (input) numerical expression
           Lowerbound,  ! (optional) numerical expression
           Scale        ! (optional) numerical expression
           )

Arguments
---------

    *Shape*
        A scalar numerical expression :math:`> 0`.

    *Lowerbound*
        A scalar numerical expression.

    *Scale*
        A scalar numerical expression :math:`> 0`.

Return Value
------------

    The function :aimms:func:`Weibull` returns a random value drawn from a Weibull
    distribution with shape *Shape* lower bound *Lowerbound*, and scale
    *Scale*.

.. note::

    The prototype of this function has changed with the introduction of
    AIMMS 3.4. In order to run models that still use the original prototype,
    the option ``Distribution_compatibility`` should be set to
    ``Aimms_3_0``. In the original function :aimms:func:`Weibull`\ (*Lowerbound*,
    *Shape*, *Scale*), the arguments were ordered differently.

.. seealso::

    The :aimms:func:`Weibull` distribution is discussed in full detail in Appendix A
    of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
