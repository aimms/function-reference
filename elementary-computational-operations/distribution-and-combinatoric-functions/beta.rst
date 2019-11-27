.. aimms:function:: Beta(ShapeAlpha, ShapeBeta, Minimum, Maximum)

.. _Beta:

Beta
====

The function :aimms:func:`Beta` draws a random value from a beta distribution.

.. code-block:: aimms

    Beta(
        ShapeAlpha,            ! (input) numerical expression
        ShapeBeta,             ! (input) numerical expression
        Minimum,               ! (optional) numerical expression
        Maximum                ! (optional) numerical expression
        )

Arguments
---------

    *ShapeAlpha*
        A scalar numerical expression :math:`> 0`.

    *ShapeBeta*
        A scalar numerical expression :math:`> 0`.

    *Minimum*
        A scalar numerical expression.

    *Maximum*
        A scalar numerical expression :math:`>`\ *min*.

Return Value
------------

    The function :aimms:func:`Beta` returns a random value drawn from a beta
    distribution with shapes *ShapeAlpha*, *ShapeBeta*, lower bound
    *Minimum* and upper bound *Maximum*.

.. note::

    The prototype of this function has changed with the introduction of
    AIMMS 3.4. In order to run models that still use the original prototype,
    the option ``Distribution_compatibility`` should be set to
    ``Aimms_3_0``. The original function :aimms:func:`Beta`\ (*ShapeAlpha*,
    *ShapeBeta*, *s*) returns a random value drawn from a beta distribution
    with shapes *ShapeAlpha*, *ShapeBeta* and scale *s*, where
    :math:`s = Maximum` and :math:`Minimum = 0`.

.. seealso::

    The :aimms:func:`Beta` distribution is discussed in full detail in Appendix A of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
