.. aimms:procedure:: GMP::Instance::SetMathematicalProgrammingType(GMP, MathematicalProgrammingType)

.. _GMP::Instance::SetMathematicalProgrammingType:

GMP::Instance::SetMathematicalProgrammingType
=============================================

The procedure :aimms:func:`GMP::Instance::SetMathematicalProgrammingType` changes
the type of a generated mathematical program from MIP into RMIP (or vice
versa), or from MINLP to RMINLP (or vice versa). Also the type can be
changed from MIQP or MIQCP to RMINLP, or from MIP or LS to LP, but not
vice versa.

.. code-block:: aimms

    GMP::Instance::SetMathematicalProgrammingType(
         GMP,                          ! (input) a generated mathematical program
         MathematicalProgrammingType   ! (input) a model type
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *MathematicalProgrammingType*
        One of the elements LP, MIP, RMIP, MINLP or RMINLP (in the set
        :aimms:set:`AllMatrixManipulationProgrammingTypes`).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::GetMathematicalProgrammingType`.
