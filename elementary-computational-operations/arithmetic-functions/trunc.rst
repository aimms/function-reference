.. aimms:function:: Trunc(x)

.. _Trunc:

Trunc
=====

.. code-block:: aimms

    Trunc(
         x       ! (input) numerical expression
         )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`Trunc` returns the truncated value of *x*:
    :math:`\textrm{sgn} \left( x \right) \cdot \lfloor \mid x \mid \rfloor`.

.. note::

    -  The function :aimms:func:`Trunc` will round to the nearest integer, if it lies
       within the equality tolerances ``equality_absolute_tolerance`` and
       ``equality_relative_ tolerance``.

    -  The function :aimms:func:`Trunc` can be used in the constraints of nonlinear
       mathematical programs. However, nonlinear solver may experience
       convergence problems around integer argument values.

    -  When the numerical expression contains a unit, the function :aimms:func:`Trunc`
       will first convert the expression to the corresponding base unit,
       before evaluating the function itself.

.. seealso::

    The functions :aimms:func:`Ceil`, :aimms:func:`Floor`, :aimms:func:`Round`, :aimms:func:`Precision`. Arithmetic
    functions are discussed in full detail in Section 6.1.4 of the Language
    Reference. Numeric tolerances are discussed in Section 6.1.4 of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
