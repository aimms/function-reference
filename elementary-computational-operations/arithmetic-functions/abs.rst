.. aimms:function:: Abs(x)

.. _Abs:

Abs
=====

.. code-block:: aimms

    Abs(
        x             ! (input) numerical expression
        )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Abs` returns the absolute value of *x*.

		
Example
-----------

.. code-block:: aimms

	_p_returnM1 := Abs(-1); ! returns 1. Abs of negative value is the negated value.
	_p_returnZ  := Abs( 0); ! returns 0. Abs of 0.0 is 0.0
	_p_returnP1 := Abs( 1); ! returns 1. Abs of positive value is the same value.


.. note::

    The function :aimms:func:`Abs` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the argument assumes values around 0.

.. seealso::

    - Arithmetic functions are discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
