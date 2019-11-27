Matrix Manipulation Functions
=============================

AIMMS supports the following matrix manipulation functions:

-  :aimms:func:`MatrixActivateRow`

-  :aimms:func:`MatrixAddColumn`

-  :aimms:func:`MatrixAddRow`

-  :aimms:func:`MatrixDeactivateRow`

-  :aimms:func:`MatrixFreezeColumn`

-  :aimms:func:`MatrixGenerate`

-  :aimms:func:`MatrixModifyCoefficient`

-  :aimms:func:`MatrixModifyColumnType`

-  :aimms:func:`MatrixModifyDirection`

-  :aimms:func:`MatrixModifyLeftHandSide`

-  :aimms:func:`MatrixModifyLowerBound`

-  :aimms:func:`MatrixModifyQuadraticCoefficient`

-  :aimms:func:`MatrixModifyRightHandSide`

-  :aimms:func:`MatrixModifyRowType`

-  :aimms:func:`MatrixModifyType`

-  :aimms:func:`MatrixModifyUpperBound`

-  :aimms:func:`MatrixRegenerateRow`

-  :aimms:func:`MatrixRestoreState`

-  :aimms:func:`MatrixSaveState`

-  :aimms:func:`MatrixSolve`

-  :aimms:func:`MatrixUnfreezeColumn`

In addition, the following function can be used the add cuts during the
solution process of a mixed integer program:

-  :aimms:func:`GenerateCut`

.. note::

    As of AIMMS release 3.5, the matrix manipulation procedures have become
    deprecated. New projects should use the GMP library instead. Please
    refer to :numref:`table:matrix.procedures` for a mapping of the
    matrix manipulation procedures to corresponding GMP functions. AIMMS
    versions prior to version 3.5, also supported a collection of matrix
    manipulation procedures with more limited functionality. Although these
    procedures will remain to be supported for all AIMMS 3.x versions, they
    have become deprecated. The deprecated manipulation procedures and their
    GMP counterparts in AIMMS 3.5 and higher are listed in :numref:`table:matrix.procedures`.

    .. _table:matrix.procedures:

.. table:: Deprecated matrix manipulation procedures 

	==================================== =========================================================
	**Deprecated Procedure**             **Counterpart**
	==================================== =========================================================
	``MatrixModifyCoefficient``          ``GMP::Coefficient::Set``
	``MatrixModifyQuadraticCoefficient`` ``GMP::Coefficient::SetQuadratic``
	``MatrixModifyRightHandSide``        ``GMP::Row::SetRightHandSide``
	``MatrixModifyLeftHandSide``         ``GMP::Row::SetLeftHandSide``
	``MatrixModifyRowType``              ``GMP::Row::SetType``
	``MatrixAddRow``                     ``GMP::Row::Add``
	``MatrixRegenerateRow``              ``GMP::Row::Generate``
	``MatrixDeactivateRow``              ``GMP::Row::Deactivate``
	``MatrixActivateRow``                ``GMP::Row::Activate``
	``MatrixModifyLowerBound``           ``GMP::Column::SetLowerBound``
	``MatrixModifyUpperBound``           ``GMP::Column::SetUpperBound``
	``MatrixModifyColumnType``           ``GMP::Column::SetType``
	``MatrixAddColumn``                  ``GMP::Column::Add``
	``MatrixFreezeColumn``               ``GMP::Column::Freeze``
	``MatrixUnfreezeColumn``             ``GMP::Column::Unfreeze``
	``MatrixModifyType``                 ``GMP::Instance::SetMathematicalProgrammingType``
	``MatrixModifyDirection``            ``GMP::Instance::SetDirection``
	``MatrixGenerate``                   ``GMP::Instance::Generate``
	``MatrixSolve``                      ``GMP::Instance::Solve``, ``GMP::SolverSession::Execute``
	``MatrixSaveState``                  ``GMP::Instance::Copy``
	``MatrixRestoreState``               ``GMP::Instance::Copy``
	==================================== =========================================================

.. toctree::
   :hidden:

   matrixactivaterow
   matrixaddcolumn
   matrixaddrow
   matrixdeactivaterow
   matrixfreezecolumn
   matrixgenerate
   matrixmodifycoefficient
   matrixmodifycolumntype
   matrixmodifydirection
   matrixmodifylefthandside
   matrixmodifylowerbound
   matrixmodifyquadraticcoefficient
   matrixmodifyrighthandside
   matrixmodifyrowtype
   matrixmodifytype
   matrixmodifyupperbound
   matrixregeneraterow
   matrixrestorestate
   matrixsavestate
   matrixsolve
   generatecut
   matrixunfreezecolumn
