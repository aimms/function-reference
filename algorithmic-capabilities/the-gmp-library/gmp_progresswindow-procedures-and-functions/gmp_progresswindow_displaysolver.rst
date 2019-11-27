.. aimms:procedure:: GMP::ProgressWindow::DisplaySolver(name, Category)

.. _GMP::ProgressWindow::DisplaySolver:

GMP::ProgressWindow::DisplaySolver
==================================

The procedure :aimms:func:`GMP::ProgressWindow::DisplaySolver` writes the solver
name to the Progress Window.

.. code-block:: aimms

    GMP::ProgressWindow::DisplaySolver(
         name,             ! (input) a solver name
         [Category]        ! (optional) a progress category
         )

Arguments
---------

    *name*
        A scalar string representing the solver name.

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    If the *Category* argument is used then the element should be created
    with the function ``GMP::SolverSession::CreateProgressCategory``.

.. seealso::

    The routines :aimms:func:`GMP::ProgressWindow::DisplaySolverStatus`, :aimms:func:`GMP::ProgressWindow::DisplayProgramStatus`, :aimms:func:`GMP::ProgressWindow::DisplayLine` and :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
