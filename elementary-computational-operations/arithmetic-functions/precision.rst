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




Example
-----------------

.. code-block:: aimms

    _p_val := 123.456789 ;
    _p_returnA := precision( _p_val, 1 ); ! precision( _p_val, 1 ) =  100
    _p_returnB := precision( _p_val, 3 ); ! precision( _p_val, 3 ) =  123
    _p_returnC := precision( _p_val, 5 ); ! precision( _p_val, 5 ) =  123.46
    _p_returnD := precision( _p_val, 7 ); ! precision( _p_val, 7 ) =  123.4568



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
    functions are discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
