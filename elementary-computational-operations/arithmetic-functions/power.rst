.. aimms:function:: Power(x, y)

.. _Power:

Power
=====

.. code-block:: aimms

    Power(
         x,      ! (input) numerical expression
         y       ! (input) numerical expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

    *y*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Power` returns :math:`x` raised to the power :math:`y`.

.. note::

    -  The following combination of arguments is allowed:

       -  :math:`x > 0`

       -  :math:`x = 0` and :math:`y > 0`

       -  :math:`x < 0` and :math:`y` integer

       In all other cases a run-time error will result.

    -  The function can be used in constraints of nonlinear mathematical
       programs.

.. seealso::

    The functions :aimms:func:`Cube`, :aimms:func:`Sqr`, and :aimms:func:`Sqrt`. Arithmetic functions
    are discussed in full detail in Section 6.1.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
