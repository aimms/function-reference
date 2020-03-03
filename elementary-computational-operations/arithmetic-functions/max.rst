.. aimms:function:: Max(x1,x2,...)

.. _Max:

Max
===

.. code-block:: aimms

    Max(
        x1,      ! (input) numerical, string or element expression
        x2,      ! (input) numerical, string or element expression
        ..
        )

Arguments
---------

    *x1,x2,...*
        Multiple numerical, string or element expressions.

Return Value
------------

    The function :aimms:func:`Max` returns the largest number, the string highest in
    the lexicographical ordering, or the element value with the highest
    ordinal value, among :math:`x1,x2,\dots`

.. note::

    The function :aimms:func:`Max` can be used in constraints of nonlinear
    mathematical programs. However, nonlinear solvers may experience
    convergence problems if the first order derivatives of two arguments
    between which the :aimms:func:`Max` function switches are discontinous.

.. seealso::

    The function :aimms:func:`Min`. Arithmetic functions are discussed in full
    detail in Section 6.1.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
