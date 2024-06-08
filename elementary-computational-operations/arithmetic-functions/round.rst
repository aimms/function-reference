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


Example
-----------------

.. code-block:: aimms

    _p_val := 123.456789 ;
    _p_returnA := round( _p_val, -1 ); ! round( _p_val, -1 ) =  120
    _p_returnB := round( _p_val,  0 ); ! round( _p_val,  0 ) =  123
    _p_returnC := round( _p_val,  2 ); ! round( _p_val,  2 ) =  123.46
    _p_returnD := round( _p_val,  5 ); ! round( _p_val,  5 ) =  123.45679


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
    functions are discussed in full detail in :ref:`sec:expr.num.functions` of the Language
    Reference.
