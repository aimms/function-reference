.. aimms:function:: Mod(x, y)

.. _Mod:

Mod
===

.. code-block:: aimms

    Mod(
        x,      ! (input) numerical expression
        y       ! (input) numerical expression
        )

Arguments
---------

    *x*
        A scalar numerical expression.

    *y*
        A scalar numerical expression unequal to 0.

Return Value
------------

    The function :aimms:func:`Mod` returns the remainder of :math:`x` after division
    by :math:`|y|`. 
    
    *   For :math:`y > 0`, the result is an integer in the range
        :math:`0,\dots,y-1` if both :math:`x` and :math:`y` are integers, or in
        the interval :math:`[0,y)` otherwise. 
    
    *   For :math:`y < 0`, the result is
        an integer in the range :math:`y-1,\dots,0` if both :math:`x` and
        :math:`y` are integers, or in the interval :math:`(y,0]` otherwise.


Example
-----------

.. code-block:: aimms

    _p_returnA := mod( 8, 3 ); ! mod( 8, 3 ) =   2
    _p_returnB := mod( 8,-3 ); ! mod( 8,-3 ) =  -1
    _p_returnC := mod(-8, 3 ); ! mod(-8, 3 ) =   1
    _p_returnD := mod(-8,-3 ); ! mod(-8,-3 ) =  -2



.. note::

    -   A run-time error results if *y* equals 0.

    -   The function :aimms:func:`Mod` can be used in constraints of mathematical
        programs. However, nonlinear solver may experience convergence
        problems if :math:`x` assumes values around multiples of :math:`y`.

.. seealso::

    -   Arithmetic functions are discussed in full detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
    -   Function :aimms:func:`Div`.