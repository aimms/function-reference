.. aimms:function:: GMP::Coefficient::GetQuadratic(GMP, column1,column2)

.. _GMP::Coefficient::GetQuadratic:

GMP::Coefficient::GetQuadratic
==============================

The function :aimms:func:`GMP::Coefficient::GetQuadratic` retrieves the value of a
quadratic product between two columns in a generated mathematical
program.

.. code-block:: aimms

    GMP::Coefficient::GetQuadratic(
         GMP,            ! (input) a generated mathematical program
         column1,        ! (input) a scalar reference or column number
         column2         ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column1,column2*
        A scalar reference to an existing column in the model or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

Return Value
------------

    The value of the specified quadratic term in the generated mathematical
    program.

.. note::

    -  If *column1* equals *column2* then AIMMS multiplies the quadratic
       coefficient by 2 before it is returned by this function.

    -  This function operates on the objective. To get a quadratic
       coefficient in a row the function ``GMP::QuadraticCoefficient::Get``
       should be used.

.. seealso::

    The routines :aimms:func:`GMP::Coefficient::SetQuadratic` and :aimms:func:`GMP::QuadraticCoefficient::Get`.
