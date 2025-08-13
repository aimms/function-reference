.. aimms:function:: Trunc(x)

.. _Trunc:

Trunc
=====

.. code-block:: aimms

    Trunc(
         x       ! (input) numerical expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Trunc` returns the truncated value of *x*:
    :math:`\textrm{sgn} \left( x \right) \cdot \lfloor \mid x \mid \rfloor`.



Example
-----------

.. code-block:: aimms

	_p_returnA := Trunc(-1.00); ! returns -1
	_p_returnB := Trunc(-0.99); ! returns  0
	_p_returnC := Trunc( 0   ); ! returns  0
	_p_returnD := Trunc( 0.99); ! returns  0




.. note::

    -  The function :aimms:func:`Trunc` will round to the nearest integer, if it lies
       within the equality tolerances ``equality_absolute_tolerance`` and
       ``equality_relative_ tolerance``.

    -  The function :aimms:func:`Trunc` can be used in the constraints of nonlinear
       mathematical programs. However, nonlinear solver may experience
       convergence problems around integer argument values.

    -  When the numerical expression contains a unit, the function :aimms:func:`Trunc`
       will first convert the expression to the corresponding base unit,
       before evaluating the function itself.

.. seealso::

    - The functions :aimms:func:`Ceil`, :aimms:func:`Floor`, :aimms:func:`Round`, :aimms:func:`Precision`. 
    - Arithmetic functions are discussed in full detail in :ref:`sec:expr.num.functions` of the Language Reference. 
    - Numeric tolerances are discussed in :ref:`sec:expr.num.functions` of the Language Reference.
