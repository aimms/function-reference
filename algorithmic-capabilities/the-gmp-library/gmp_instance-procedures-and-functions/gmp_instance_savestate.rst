.. aimms:procedure:: GMP::Instance::SaveState(GMP, state)

.. _GMP::Instance::SaveState:

GMP::Instance::SaveState
========================

With the procedure :aimms:func:`GMP::Instance::SaveState` you can save the current state of
a generated mathematical program. Later on, after manipulating the generated mathematical
program, you can restore this state by calling :aimms:func:`GMP::Instance::RestoreState`.

.. code-block:: aimms

    GMP::Instance::SaveState(
         GMP,             ! (input) a generated mathematical program
         state            ! (output) an integer scalar parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *state*
        On return, contains a positive integer value assigned to the state.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    States are numbered from 1 upwards by AIMMS.

.. seealso::

    - The procedure :aimms:func:`GMP::Instance::RestoreState`.
