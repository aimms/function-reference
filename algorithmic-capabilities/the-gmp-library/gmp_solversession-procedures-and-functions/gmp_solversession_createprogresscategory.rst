.. aimms:function:: GMP::SolverSession::CreateProgressCategory(solverSession, Name, Size)

.. _GMP::SolverSession::CreateProgressCategory:

GMP::SolverSession::CreateProgressCategory
==========================================

| The function :aimms:func:`GMP::SolverSession::CreateProgressCategory` creates a
  new progress category for a solver session. This progress category can
  be used to display solver (session) related information in the
  Progress Window.
| There are three levels of progress categories for solver information.
  By default all solver progress will be displayed in the general AIMMS
  progress category for solver progress. If a progress category was
  created for the GMP with procedure
  ``GMP::Instance::CreateProgressCategory``, then all solver progress
  related to that GMP will by default be displayed in the solver
  progress category of the GMP. For displaying solver session progress
  in a separated category the function
  :aimms:func:`GMP::SolverSession::CreateProgressCategory` can be used.

.. code-block:: aimms

    GMP::SolverSession::CreateProgressCategory(
         solverSession,    ! (input) a solver session
         [Name],           ! (optional) a string expression
         [Size]            ! (optional) an integer expession
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *Name*
        A string that holds the name of the progress category.

    *Size*
        The number of lines in the progress category. The default is 0 meaning
        that the size of the progress window will be automatically adjusted to
        the number of progress lines used by the solver.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllProgressCategories`.

.. note::

    -  If the *Name* argument is not specified then the name of the solver
       session will be used to name the element in the set :aimms:set:`AllProgressCategories`.

    -  The information displayed in the solver session progress window can
       be controlled by using the procedures
       ``GMP::ProgressWindow::DisplayLine`` and
       ``GMP::ProgressWindow::FreezeLine``.

    -  A progress category created before for the solver session will be
       deleted.

    -  The procedure ``GMP::ProgressWindow::Transfer`` can be used to share
       a progress category among several solver sessions.

.. seealso::

    The routines :aimms:func:`GMP::ProgressWindow::CreateProgressCategory`, :aimms:func:`GMP::ProgressWindow::DeleteCategory`, :aimms:func:`GMP::ProgressWindow::DisplayLine`, :aimms:func:`GMP::ProgressWindow::FreezeLine`, :aimms:func:`GMP::ProgressWindow::UnfreezeLine` and
    :aimms:func:`GMP::ProgressWindow::Transfer`.
