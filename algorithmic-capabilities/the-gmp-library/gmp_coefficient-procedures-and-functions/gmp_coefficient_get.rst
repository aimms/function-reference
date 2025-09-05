.. aimms:function:: GMP::Coefficient::Get(GMP, row, column)

.. _GMP::Coefficient::Get:

GMP::Coefficient::Get
=====================

The function :aimms:func:`GMP::Coefficient::Get` retrieves a (linear) coefficient
in a generated mathematical program.

.. code-block:: aimms

    GMP::Coefficient::Get(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the model or the number of that
        row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the number of
        rows in the matrix.

    *column*
        A scalar reference to an existing column in the model or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The value of the specified coefficient in the generated mathematical
    program.

.. note::

    In case the generated mathematical program is nonlinear, this function
    will return 0 if the column is part of a nonlinear term in the row.
    However, if the row is pure quadratic then this function will return the
    linear coefficient value for a quadratic column.

Example
-------

Consider a GMP containing a constraint ``e1`` with definition
``2*x1 + 3*x2 + x2^3 = 0``. Then ``GMP::Coefficient::Get(GMP,e1,x1)``
will return 2. Because column ``x2`` is part of the nonlinear term
``x2^3``, ``GMP::Coefficient::Get(GMP,e1,x2)`` will return 0.

.. seealso::

    - The routines :aimms:func:`GMP::Coefficient::Set` and :aimms:func:`GMP::QuadraticCoefficient::Get`.
