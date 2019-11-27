.. aimms:set:: CurrentSolver

.. _CurrentSolver:

CurrentSolver
=============

The predefined element parameter :aimms:set:`CurrentSolver` contains, for every
mathematical programming type, the name of the solver that AIMMS will
currently use to solve models of that type.

.. code-block:: aimms

        ElementParameter CurrentSolver {
            IndexDomain  :  IndexMathematicalProgrammingTypes;
            Range        :  AllSolvers;
        }

Definition
----------

    The contents of the element parameter :aimms:set:`CurrentSolver` are, for all
    types of mathematical programs, the names of the currently active solver
    for solving mathematical programs of each type, as set through the
    **Solver Configuration** dialog box.

Updatability
------------

    The value of :aimms:set:`CurrentSolver` can also be modified programmatically
    from within an AIMMS model, and then determines the solver that will be
    used to solve subsequent problems of the specified type. Modifying the
    values of :aimms:set:`CurrentSolver` will, however, not modify the (default)
    settings in the **Solver Configuration** dialog box, that will be loaded
    at startup.

.. seealso::

    -  The sets :aimms:set:`AllMathematicalProgrammingTypes` and :aimms:set:`AllSolvers`.

    -  Solver configuration is discussed in full detail in Section 20.3 of
       the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
