.. aimms:procedure:: GMP::Column::GetUpperBoundRaw(GMP, colSet, ubs)

.. _GMP::Column::GetUpperBoundRaw:

GMP::Column::GetUpperBoundRaw
=============================

The procedure :aimms:procedure:`GMP::Column::GetUpperBoundRaw` retrieves 
a collection of upper bound values corresponding to a given set of columns 
in the generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetUpperBoundRaw(
         GMP,            ! (input) a generated mathematical program
         colSet,         ! (input) a subset of Integers
         ubs             ! (output) a real-valued parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *colSet*
        A subset of the set Integers, representing a set of column numbers. 
        Each column number should be in the range :math:`\{ 0 .. n-1 \}` 
        where :math:`n` is the number of columns in the matrix.

    *ubs*
        A real-valued parameter over colSet indicating the upper bound 
        values of each column in colSet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If a column has a unit then the scaled upper bound is retrieved
       (without unit).
       
    -  This procedure is much more efficient than calling the function 
       :aimms:func:`GMP::Column::GetUpperBound` to get the upper bound of 
       each column in colSet individually.

.. seealso::

    - The routine :aimms:func:`GMP::Column::GetUpperBound` and :aimms:func:`GMP::Column::GetLowerBoundRaw`.
