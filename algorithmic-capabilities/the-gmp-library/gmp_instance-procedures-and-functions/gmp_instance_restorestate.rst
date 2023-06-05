.. aimms:procedure:: GMP::Instance::RestoreState(GMP, state)

.. _GMP::Instance::RestoreState:

GMP::Instance::RestoreState
===========================

With procedure :aimms:func:`GMP::Instance::RestoreState` you can restore the state of a
generated mathematical program as it was on the moment that you called
:aimms:func:`GMP::Instance::SaveState`.

.. code-block:: aimms

    GMP::Instance::RestoreState(
         GMP,             ! (input) a generated mathematical program
         state            ! (input) an integer scalar parameter
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *state*
        The value corresponding to a state that you want to restore.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The procedure :aimms:func:`GMP::Instance::SaveState`.
