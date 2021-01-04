.. aimms:function:: Min(x1,x2,$\dots$)

.. _Min:

Min
===

.. code-block:: aimms

    Min(
        x1,      ! (input) numerical, string or element expression
        x2,      ! (input) numerical, string or element expression
        ..
        )

Arguments
---------

    *x1,x2,$\dots$*
        Multiple numerical, string or element expressions.

Return Value
------------

    The function :aimms:func:`Min` returns the smallest number, the string lowest in
    the lexicographical ordering, or the element value with the lowest
    ordinal value, among :math:`x1,x2,\dots`

.. note::

    The function :aimms:func:`Min` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the first order derivatives of two arguments
    between which the :aimms:func:`Min` function switches are discontinous.

.. seealso::

    The function :aimms:func:`Max`. Arithmetic functions are discussed in full
    detail in :ref:`sec:expr.num.functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
