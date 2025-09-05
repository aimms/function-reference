.. aimms:procedure:: GMP::Column::GetLowerBoundRaw(GMP, colSet, lbs)

.. _GMP::Column::GetLowerBoundRaw:

GMP::Column::GetLowerBoundRaw
=============================

The procedure :aimms:procedure:`GMP::Column::GetLowerBoundRaw` retrieves 
a collection of lower bound values corresponding to a given set of columns 
in the generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetLowerBoundRaw(
         GMP,            ! (input) a generated mathematical program
         colSet,         ! (input) a subset of Integers
         lbs             ! (output) a real-valued parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *colSet*
        A subset of the set Integers, representing a set of column numbers. 
        Each column number should be in the range :math:`\{ 0 .. n-1 \}` 
        where :math:`n` is the number of columns in the matrix.

    *lbs*
        A real-valued parameter over colSet indicating the lower bound 
        values of each column in colSet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If a column has a unit then the scaled lower bound is retrieved
       (without unit).
    
    -  This procedure is much more efficient than calling the function 
       :aimms:func:`GMP::Column::GetLowerBound` to get the lower bound of 
       each column in colSet individually.

.. seealso::

    - The routine :aimms:func:`GMP::Column::GetLowerBound` and :aimms:func:`GMP::Column::GetUpperBoundRaw`.
