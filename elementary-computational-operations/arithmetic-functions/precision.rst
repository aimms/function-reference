.. aimms:function:: Precision(x, y)

.. _Precision:

Precision
=========

.. code-block:: aimms

    Precision(
         x,            ! (input) numerical expression
         y             ! (input) integer expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

    *y*
        An integer expression.

Return Value
------------

    The function :aimms:func:`Precision` returns *x* rounded to *y* significant
    digits.

.. note::

    -  The function :aimms:func:`Precision` can be used in constraints of nonlinear
       mathematical programs. However, nonlinear solvers may experience
       convergence problems around the discontinuities of the :aimms:func:`Precision`
       function.

    -  When the numerical expression contains a unit, the function
       :aimms:func:`Precision` will first convert the expression to the corresponding
       base unit, before evaluating the function itself.

.. seealso::

    The functions :aimms:func:`Round`, :aimms:func:`Ceil`, :aimms:func:`Floor`, :aimms:func:`Trunc`. Arithmetic
    functions are discussed in full detail in Section 6.1.4 of the Language
    Reference.
