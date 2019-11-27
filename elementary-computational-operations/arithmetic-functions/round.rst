.. aimms:function:: Round(x[, decimals])

.. _Round:

Round
=====

.. code-block:: aimms

    Round(
         x,            ! (input) numerical expression
         decimals      ! (optional) integer expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

    *decimals (optional)*
        An integer expression.

Return Value
------------

    The function :aimms:func:`Round` returns the integer value nearest to *x*. In the
    presence of the optional argument *n* the function :aimms:func:`Round` returns the
    value of *x* rounded to *n* decimal places left (:math:`decimals < 0`)
    or right (:math:`decimals > 0`) of the decimal point.

.. note::

    -  The function :aimms:func:`Round` can be used in constraints of nonlinear
       mathematical programs. However, nonlinear solvers may experience
       convergence problems around the discontinuities of the :aimms:func:`Round`
       function.

    -  When the numerical expression contains a unit, the function :aimms:func:`Round`
       will first convert the expression to that unit, before evaluating the
       function itself. See also the option ``rounding compatibility`` in
       the option category ``backward compatibility``.

.. seealso::

    The functions :aimms:func:`Precision`, :aimms:func:`Ceil`, :aimms:func:`Floor`, :aimms:func:`Trunc`. Arithmetic
    functions are discussed in full detail in Section 6.1.4 of the Language
    Reference.
