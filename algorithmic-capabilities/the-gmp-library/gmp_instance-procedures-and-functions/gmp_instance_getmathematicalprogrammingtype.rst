.. aimms:function:: GMP::Instance::GetMathematicalProgrammingType(GMP)

.. _GMP::Instance::GetMathematicalProgrammingType:

GMP::Instance::GetMathematicalProgrammingType
=============================================

The function :aimms:func:`GMP::Instance::GetMathematicalProgrammingType` returns
the model type of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetMathematicalProgrammingType(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the model type as an element in :aimms:set:`AllMathematicalProgrammingTypes`.

.. seealso::

    The function :aimms:func:`GMP::Instance::Generate` and the procedure :aimms:func:`GMP::Instance::SetMathematicalProgrammingType`.
