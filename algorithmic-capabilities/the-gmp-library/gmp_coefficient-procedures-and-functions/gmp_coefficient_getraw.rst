.. aimms:procedure:: GMP::Coefficient::GetRaw(GMP, rowSet, colSet, coef)

.. _GMP::Coefficient::GetRaw:

GMP::Coefficient::GetRaw
=============================

The procedure :aimms:func:`GMP::Coefficient::GetRaw` retrieves a collection of (linear) coefficients
in a generated mathematical program. The retrieved collection is indicated by the given row and column sets.

.. code-block:: aimms

    GMP::Coefficient::GetRaw(
         GMP,            ! (input)  a generated mathematical program
         rowSet,         ! (input)  a subset of Integers
         colSet,         ! (input)  a subset of Integers
         coef            ! (output) a real-valued parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set Integers, representing a set of row numbers. Each 
        row number should be in the range :math:`\{ 0 .. m-1 \}` where 
        :math:`m` is the number of rows in the matrix.

    *colSet*
        A subset of the set Integers, representing a set of column numbers. 
        Each column should be in the range :math:`\{ 0 .. n-1 \}` where 
        :math:`n` is the number of columns in the matrix.

    *coef*
        A real-valued parameter over rowSet and colSet indicating the
        coefficient values for each row and column in rowSet and colSet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    This procedure is much more efficient than calling the function 
    :aimms:func:`GMP::Coefficient::Get` to get the coefficients of each 
    row and column in rowSet and colSet individually.

.. seealso::

    - The routine :aimms:func:`GMP::Coefficient::Get`.
