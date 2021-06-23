.. aimms:procedure:: MatrixAddColumn(MP, column)

.. _MatrixAddColumn:

MatrixAddColumn
===============

The procedure :aimms:func:`MatrixAddColumn` adds a column to the matrix.

.. code-block:: aimms

    MatrixAddColumn(
         MP,             ! (input) a mathematical program
         column          ! (input) a scalar value
         )

Arguments
---------

    *MP*
        A mathematical program that was previously solved. The mathematical
        program should be a linear or mixed-integer linear programming model.

    *column*
        A scalar reference to an existing column name in the model.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Coefficients for this column can be added to the matrix by using the
       procedure ``MatrixModifyCoefficient``. After calling
       :aimms:func:`MatrixAddColumn` the type and the lower and upper bound of the
       column are set according to the definition of the corresponding
       symbolic variable. By using the procedures
       ``MatrixModifyColumnType``, ``MatrixModifyLowerBound`` and
       ``MatrixModifyUpperBound`` the column type and the lower and upper
       bound can be changed.

    -  As of AIMMS release 3.5, the matrix manipulation procedures have
       become deprecated. New projects should use the GMP library instead.
       Please refer to :numref:`table:matrix.procedures` for a mapping
       of the matrix manipulation procedures to corresponding GMP
       procedures.

.. seealso::

    The procedures :aimms:func:`MatrixModifyCoefficient`, :aimms:func:`MatrixModifyColumnType`, :aimms:func:`MatrixModifyLowerBound`, :aimms:func:`MatrixModifyUpperBound`. Matrix
    manipulation routines are discussed in more detail in :doc:`optimization-modeling-components/implementing-advanced-algorithms-for-mathematical-programs/index` of the
     Language Reference.
