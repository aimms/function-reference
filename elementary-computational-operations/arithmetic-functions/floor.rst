.. aimms:function:: Floor(x)

.. _Floor:

Floor
=====

.. code-block:: aimms

    Floor(
         x             ! (input) numerical expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Floor` returns the largest integer value :math:`\leq`
    *x*.

.. note::

    -  The function :aimms:func:`Floor` will round to the nearest integer, if it lies
       within the equality tolerances ``equality_absolute_tolerance`` and
       ``equality_relative_tolerance``.

    -  The function :aimms:func:`Floor` can be used in the constraints of nonlinear
       mathematical programs. However, nonlinear solvers may experience
       convergence problems around integer values.

    -  When the numerical expression contains a unit, the function :aimms:func:`Floor`
       will first convert the expression to the corresponding base unit,
       before evaluating the function itself.

.. seealso::

    The functions :aimms:func:`Ceil`, :aimms:func:`Round`, :aimms:func:`Precision`, :aimms:func:`Trunc`. Arithmetic
    functions are discussed in full detail in :ref:`sec:expr.num.functions` of the Language
    Reference. Numeric tolerances are discussed in :ref:`sec:expr.num.functions` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
