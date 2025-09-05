.. aimms:procedure:: GMP::Coefficient::SetQuadratic(GMP, column1,Column2, value)

.. _GMP::Coefficient::SetQuadratic:

GMP::Coefficient::SetQuadratic
==============================

The procedure :aimms:func:`GMP::Coefficient::SetQuadratic` sets the value of a
quadratic product between two columns in a generated mathematical
program.

.. code-block:: aimms

    GMP::Coefficient::SetQuadratic(
         GMP,            ! (input) a generated mathematical program
         column1,        ! (input) a scalar value or column number
         column2,        ! (input) a scalar value or column number
         value           ! (input) a scalar numerical value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column1,column2*
        A scalar reference to an existing column in the model or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        A scalar numerical value indicating the value for the quadratic term.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If *column1* equals *column2* then AIMMS multiplies the quadratic
       coefficient by 0.5 before it is stored (and passed to the solver).

    -  This procedure operates on the objective. To set a quadratic
       coefficient in a row the procedure :aimms:func:`GMP::QuadraticCoefficient::Set`
       should be used.

.. seealso::

    - The routines :aimms:func:`GMP::Coefficient::GetQuadratic` and :aimms:func:`GMP::QuadraticCoefficient::Set`.
