.. aimms:function:: Ceil(x)

.. _Ceil:

Ceil
====

.. code-block:: aimms

    Ceil(
        x             ! (input) numerical expression
        )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Ceil` returns the smallest integer value :math:`\geq`
    *x*.

.. note::

    -  The function :aimms:func:`Ceil` will round to the nearest integer, if it lies
       within the equality tolerances ``equality_absolute_tolerance`` and
       ``equality_relative_tolerance``.

    -  The function :aimms:func:`Ceil` can be used in the constraints of nonlinear
       mathematical programs. However, nonlinear solvers may experience
       convergence problems around integer values.

    -  When the numerical expression contains a unit, the function :aimms:func:`Ceil`
       will first convert the expression to the corresponding base unit,
       before evaluating the function itself.

.. seealso::

    The functions :aimms:func:`Floor`, :aimms:func:`Round`, :aimms:func:`Precision`, :aimms:func:`Trunc`. Arithmetic
    functions are discussed in full detail in :ref:`sec:expr.num.functions` of the Language
    Reference. Numeric tolerances are discussed in :ref:`sec:expr.num.functions` of the
     Language Reference.
