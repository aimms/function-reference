.. aimms:function:: GMP::Instance::Copy(GMP, name)

.. _GMP::Instance::Copy:

GMP::Instance::Copy
===================

The function :aimms:func:`GMP::Instance::Copy` creates a copy of a generated
mathematical program and an associated new element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

.. code-block:: aimms

    GMP::Instance::Copy(
         GMP,            ! (input) a generated mathematical program
         name            ! (input) a string expression
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that contains the name for the copy of the generated
        mathematical program.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  The *name* argument should be different from the name of the original
       generated mathematical program.

    -  If an element with name specified by the *name* argument is already
       present in the set :aimms:set:`AllGeneratedMathematicalPrograms` then the corresponding generated
       mathematical program will be replaced (or updated in case the same
       symbolic mathematical program is involved).

    -  All solutions in the solution repository of the generated
       mathematical program are also copied.

    -  The solver selection as specified by :aimms:func:`GMP::Instance::SetSolver` (if
       any) will not be copied.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Rename` and :aimms:func:`GMP::Instance::SetSolver`.
