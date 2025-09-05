.. aimms:procedure:: GMP::Coefficient::GetMinAndMax(GMP, rowSet, colSet, minCoef, maxCoef, absSense)

.. _GMP::Coefficient::GetMinAndMax:

GMP::Coefficient::GetMinAndMax
==============================

The procedure :aimms:func:`GMP::Coefficient::GetMinAndMax` determines the minimum and maximum value of (linear) coefficients
in a generated mathematical program. The domain of this evaluation is indicated by the given row and column sets.

.. code-block:: aimms

    GMP::Coefficient::GetMinAndMax(
         GMP,            ! (input)  a generated mathematical program
         rowSet,         ! (input)  a subset of Integers
         colSet,         ! (input)  a subset of Integers
         minCoef,        ! (output) a real-valued parameter
         maxCoef,        ! (output) a real-valued parameter
         [absSense]      ! (optional, default 1) a scalar value
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

    *minCoef*
        A real-valued parameter indicating the minimum coefficient in the *GMP*.
        
    *maxCoef*
        A real-valued parameter indicating the maximum coefficient in the *GMP*.
        
    *absSense*
        A binary scalar indicating whether the absolute value of coefficients
        should be taken into consideration when determining minimum and maximum 
        coefficients. The default is 1, meaning that the absolute value of 
        coefficients are considered.
    

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    This procedure neglects zero coefficients in determining the minimum and maximum values.
    
.. seealso::

    - The routines :aimms:func:`GMP::Coefficient::Get` and :aimms:func:`GMP::Coefficient::GetMultiRaw`.
