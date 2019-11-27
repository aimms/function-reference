.. aimms:function:: Abs(x)

.. _Abs:

Abs
===

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

.. note::

    The function :aimms:func:`Abs` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the argument assumes values around 0.

.. seealso::

    Arithmetic functions are discussed in full detail in Section 6.1.4 of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
