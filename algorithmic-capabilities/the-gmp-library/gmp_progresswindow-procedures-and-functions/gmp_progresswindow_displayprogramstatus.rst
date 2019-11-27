.. aimms:procedure:: GMP::ProgressWindow::DisplayProgramStatus(status, Category, lineNo)

.. _GMP::ProgressWindow::DisplayProgramStatus:

GMP::ProgressWindow::DisplayProgramStatus
=========================================

The procedure :aimms:func:`GMP::ProgressWindow::DisplayProgramStatus` writes the
program status (or model status) to the Progress Window.

.. code-block:: aimms

    GMP::ProgressWindow::DisplayProgramStatus(
         status,           ! (input) a status
         [Category],       ! (optional) a progress category
         [lineNo]          ! (optional) a line number
         )

Arguments
---------

    *status*
        An element in the set :aimms:set:`AllSolutionStates`.

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

    *lineNo*
        The number of the line in which the program status has to be displayed.
        The default is 7.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the *Category* argument is used then the element should be created
       with the function ``GMP::SolverSession::CreateProgressCategory``.

    -  The program status can also be displayed by using the procedure
       ``GMP::ProgressWindow::DisplayLine`` with title 'Program Status'.

.. seealso::

    The routines :aimms:func:`GMP::Solution::GetProgramStatus`, :aimms:func:`GMP::ProgressWindow::DisplayLine`, :aimms:func:`GMP::ProgressWindow::DisplaySolverStatus` and :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
