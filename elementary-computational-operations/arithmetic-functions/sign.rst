.. aimms:function:: Sign(x)

.. _Sign:

Sign
====

.. code-block:: aimms

    Sign(
        x             ! (input) numerical expression
        )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Sign` returns :math:`+1` if :math:`x > 0`, :math:`-1` if
    :math:`x < 0` and 0 if :math:`x = 0`.


Example
-----------------

.. code-block:: aimms

    _p_returnM1 := Sign(-3); ! returns -1. Sign of negative value is -1.
    _p_returnZ  := Sign( 0); ! returns  0. Sign of 0.0 is 0.0
    _p_returnP1 := Sign( 3); ! returns  1. Sign of positive value is 1.


.. note::

    The function :aimms:func:`Sign` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solver may experience
    convergence problems round 0.

.. seealso::

    The function :aimms:func:`Abs`. Arithmetic functions are discussed in full
    detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
