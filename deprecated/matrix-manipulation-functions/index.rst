Matrix Manipulation Procedures
==============================

The matrix manipulation procedures have been deprecated since AIMMS version 3.5,
and have been removed in AIMMS version 4.96.
New projects should use the GMP library instead. Please
refer to :numref:`table:matrix.procedures` for a mapping of the
matrix manipulation procedures to corresponding GMP procedures. 

    .. _table:matrix.procedures:

.. table:: Removed matrix manipulation procedures 

	==================================== =========================================================
	**Deprecated Procedure**             **Counterpart**
	==================================== =========================================================
	``MatrixModifyCoefficient``          :aimms:func:`GMP::Coefficient::Set`
	``MatrixModifyQuadraticCoefficient`` :aimms:func:`GMP::Coefficient::SetQuadratic`
	``MatrixModifyRightHandSide``        :aimms:func:`GMP::Row::SetRightHandSide`
	``MatrixModifyLeftHandSide``         :aimms:func:`GMP::Row::SetLeftHandSide`
	``MatrixModifyRowType``              :aimms:func:`GMP::Row::SetType`
	``MatrixAddRow``                     :aimms:func:`GMP::Row::Add`
	``MatrixRegenerateRow``              :aimms:func:`GMP::Row::Generate`
	``MatrixDeactivateRow``              :aimms:func:`GMP::Row::Deactivate`
	``MatrixActivateRow``                :aimms:func:`GMP::Row::Activate`
	``MatrixModifyLowerBound``           :aimms:func:`GMP::Column::SetLowerBound`
	``MatrixModifyUpperBound``           :aimms:func:`GMP::Column::SetUpperBound`
	``MatrixModifyColumnType``           :aimms:func:`GMP::Column::SetType`
	``MatrixAddColumn``                  :aimms:func:`GMP::Column::Add`
	``MatrixFreezeColumn``               :aimms:func:`GMP::Column::Freeze`
	``MatrixUnfreezeColumn``             :aimms:func:`GMP::Column::Unfreeze`
	``MatrixModifyType``                 :aimms:func:`GMP::Instance::SetMathematicalProgrammingType`
	``MatrixModifyDirection``            :aimms:func:`GMP::Instance::SetDirection`
	``MatrixGenerate``                   :aimms:func:`GMP::Instance::Generate`
	``MatrixSolve``                      :aimms:func:`GMP::Instance::Solve`
	``MatrixSaveState``                  :aimms:func:`GMP::Instance::SaveState`
	``MatrixRestoreState``               :aimms:func:`GMP::Instance::RestoreState`
	==================================== =========================================================
