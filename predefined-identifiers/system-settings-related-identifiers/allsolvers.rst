.. aimms:set:: AllSolvers

.. _AllSolvers:

AllSolvers
==========

The predefined set :aimms:set:`AllSolvers` contains the names of all types of
solvers associated with the AIMMS system installed on a particular
computer.

.. code-block:: aimms

        Set AllSolvers {
            Index      :  IndexSolvers;
        }

Definition
----------

    The contents of the set :aimms:set:`AllSolvers` is the collection of all types of
    solvers linked to a particular AIMMS system through the **Solver
    Configuration** dialog box.

Updatability
------------

    The contents of the set can only be modified through the **Solver
    Configuration** dialog box.

.. note::

    The set :aimms:set:`AllSolvers` can be used in applications to test whether one
    or more solvers are available, as illustrated in the AIMMS example
    ``Economic Exchange Equilibrium``.

.. seealso::

    -  Solver configuration is discussed in full detail in Section 20.3 of
       the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.

    -  The parameter :aimms:set:`CurrentSolver`.

    -  The functions :aimms:func:`GMP::Instance::CreateSolverSession` and :aimms:func:`GMP::Instance::GetSolver`
