.. aimms:set:: AllSolverInterrupts

.. _AllSolverInterrupts:

AllSolverInterrupts
===================

The predefined set :aimms:set:`AllSolverInterrupts` contains the names of all
causes for a callback.

.. code-block:: aimms

        Set AllSolverInterrupts {
            Index      :  IndexSolverInterrupts;
            Definition :  {
                data { AddCut, Branch, Candidate, Heuristic, Incumbent,
                       Iterations, StatusChange, AddLazyConstraint,
                       Finished, Time }
            }
        }

Definition
----------

    The set :aimms:set:`AllSolverInterrupts` contains the names of all causes for a
    callback.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    If you have installed the same callback procedure for several callbacks,
    you can call the function
    ``GMP::SolverSession::GetCallbackInterruptStatus``, which returns an
    element into the set :aimms:set:`AllSolverInterrupts`, to obtain the particular
    callback for which your callback procedure was called.

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackAddLazyConstraint`, :aimms:func:`GMP::Instance::SetCallbackBranch`, :aimms:func:`GMP::Instance::SetCallbackCandidate`, :aimms:func:`GMP::Instance::SetCallbackHeuristic`,
    :aimms:func:`GMP::Instance::SetCallbackIncumbent`, :aimms:func:`GMP::Instance::SetCallbackStatusChange`, :aimms:func:`GMP::Instance::SetCallbackTime`, and :aimms:func:`GMP::SolverSession::GetCallbackInterruptStatus`.
