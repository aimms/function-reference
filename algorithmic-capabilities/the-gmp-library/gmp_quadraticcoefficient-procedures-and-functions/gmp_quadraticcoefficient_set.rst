.. aimms:procedure:: GMP::QuadraticCoefficient::Set(GMP, row, column1, column2, value)

.. _GMP::QuadraticCoefficient::Set:

GMP::QuadraticCoefficient::Set
==============================

The procedure :aimms:func:`GMP::QuadraticCoefficient::Set` sets the value for a
quadratic coefficient in a quadratic row of a generated mathematical
program.

.. code-block:: aimms

    GMP::QuadraticCoefficient::Set(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference
         column1,        ! (input) a scalar reference
         column2,        ! (input) a scalar reference
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix.

    *column1*
        A scalar reference to an existing column in the matrix.

    *column2*
        A scalar reference to an existing column in the matrix.

    *value*
        A scalar numerical value indicating the value for the coefficient.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    If *column1* equals *column2* then AIMMS multiplies the quadratic
    coefficient by 0.5 before it is stored (and passed to the solver).

.. seealso::

    The routines :aimms:func:`GMP::QuadraticCoefficient::Get`, :aimms:func:`GMP::Coefficient::GetQuadratic` and :aimms:func:`GMP::Coefficient::SetQuadratic`.
