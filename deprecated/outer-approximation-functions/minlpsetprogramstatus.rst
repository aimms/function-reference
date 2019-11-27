.. aimms:function:: MINLPSetProgramStatus(ProgramStatus)

.. _MINLPSetProgramStatus:

MINLPSetProgramStatus
=====================

The procedure :aimms:func:`MINLPSetProgramStatus` sets the program status for the
MINLP problem.

.. code-block:: aimms

    MINLPSetProgramStatus(
         ProgramStatus      ! (input) element parameter into AllSolutionStates
         )

Arguments
---------

    *ProgramStatus*
        Element parameter into :aimms:set:`AllSolutionStates` that sets the program status for the
        MINLP problem.

Return Value
------------

    ``MINLPSetProgramStatus()`` has no return value.
