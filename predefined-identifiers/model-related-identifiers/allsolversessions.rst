.. aimms:set:: AllSolverSessions

.. _AllSolverSessions:

AllSolverSessions
=================

The predefined set :aimms:set:`AllSolverSessions` contains the names of all
solver sessions associated with generated mathematical programs in your
model.

.. code-block:: aimms

        Set AllSolverSessions {
            SubsetOf     :  AllSolverSessionCompletionObjects;
            Index        :  IndexSolverSessions;
        }

Definition
----------

    The set :aimms:set:`AllSolverSessions` contains the names of all solver sessions
    associated with generated mathematical programs in your model. Solver
    sessions are created through the ``SOLVE`` statement, and the functions
    ``GMP::Instance::Solve`` and ``GMP::Instance::CreateSolverSession``.

Updatability
------------

    The contents of :aimms:set:`AllSolverSessions` can only be modified
    programmatically through the ``SOLVE`` statement, and the functions
    ``GMP::Instance::Solve``, ``GMP::Instance::CreateSolverSession`` and
    ``GMP::Instance::DeleteSolverSession``.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::Instance::DeleteSolverSession`, and the predeclared
    identifier :aimms:set:`AllSolverSessionCompletionObjects`.
