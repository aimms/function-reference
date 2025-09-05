.. aimms:procedure:: GMP::Row::GetRightHandSideRaw(GMP, rowSet, rhs)

.. _GMP::Row::GetRightHandSideRaw:

GMP::Row::GetRightHandSideRaw
=============================

The procedure :aimms:procedure:`GMP::Row::GetRightHandSideRaw` retrieves 
a collection of right-hand-side values corresponding to a given set of row 
numbers in the generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetRightHandSideRaw(
         GMP,            ! (input)  a generated mathematical program
         rowSet,         ! (input)  a subset of Integers
         rhs             ! (output) a real-valued parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *rowSet*
        A subset of the set Integers, representing a set of row numbers. 
        Each row number should be in the range :math:`\{ 0 .. m-1 \}` 
        where :math:`m` is the number of rows in the matrix.

    *rhs*
        A real-valued parameter over rowSet indicating the right hand 
        side values of each row in rowSet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If a row has a unit then the scaled right-hand-side value is 
       retrieved (without unit).

    -  This procedure is much more efficient than calling the function 
       :aimms:func:`GMP::Row::GetRightHandSide` to get the right hand 
       side of each row in rowSet individually.

.. seealso::

    - The routine :aimms:func:`GMP::Row::GetRightHandSide`.
