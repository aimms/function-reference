.. aimms:function:: GMP::QuadraticCoefficient::Get(GMP, row, column1, column2)

.. _GMP::QuadraticCoefficient::Get:

GMP::QuadraticCoefficient::Get
==============================

The function :aimms:func:`GMP::QuadraticCoefficient::Get` retrieves a quadratic
coefficient in a quadratic row of a generated mathematical program.

.. code-block:: aimms

    GMP::QuadraticCoefficient::Get(
         GMP,             ! (input) a generated mathematical program
         row,             ! (input) a scalar reference
         column1,         ! (input) a scalar reference
         column2          ! (input) a scalar reference
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

Return Value
------------

    The value of the specified quadratic coefficient in the quadratic row.

.. note::

    If *column1* equals *column2* then AIMMS multiplies the quadratic
    coefficient by 2 before it is returned by this function.

.. seealso::

    The routines :aimms:func:`GMP::QuadraticCoefficient::Set`, :aimms:func:`GMP::Coefficient::GetQuadratic` and :aimms:func:`GMP::Coefficient::SetQuadratic`.
