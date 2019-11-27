.. aimms:function:: Div(x, y)

.. _Div:

Div
===

.. code-block:: aimms

    Div(
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

    The function :aimms:func:`Div` returns :math:`x` divided by :math:`y` rounded down
    to an integer.

.. note::

    A run-time error results if *y* equals 0.

.. seealso::

    Arithmetic functions are discussed in full detail in Section 6.1.4 of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
