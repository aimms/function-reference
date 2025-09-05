.. aimms:function:: GMP::Instance::GetSymbolicMathematicalProgram(GMP)

.. _GMP::Instance::GetSymbolicMathematicalProgram:

GMP::Instance::GetSymbolicMathematicalProgram
=============================================

The function :aimms:func:`GMP::Instance::GetSymbolicMathematicalProgram` returns
for a generated mathematical program the originating symbolic
mathematical program.

.. code-block:: aimms

    GMP::Instance::GetSymbolicMathematicalProgram(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the symbolic mathematical program as an element of
    :aimms:set:`AllMathematicalPrograms`.

.. seealso::

    - The function :aimms:func:`GMP::Instance::Generate`.
