.. aimms:procedure:: GMP::ProgressWindow::FreezeLine(lineNo, totalFreeze, Category)

.. _GMP::ProgressWindow::FreezeLine:

GMP::ProgressWindow::FreezeLine
===============================

The procedure :aimms:func:`GMP::ProgressWindow::FreezeLine` freezes (or locks) a
line in the Progress Window.

.. code-block:: aimms

    GMP::ProgressWindow::FreezeLine(
         lineNo,           ! (input) a line number
         [totalFreeze],    ! (optional) a binary
         [Category]        ! (optional) a progress category
         )

Arguments
---------

    *lineNo*
        The number of the line that should be frozen.

    *totalFreeze*
        If it equals 1 (the default) then the line will never change (untill the
        procedure ``GMP::ProgressWindow::UnfreezeLine`` is called). If it equals
        0 then the line will only change if a ``GMP::ProgressWindow`` procedure
        is called for this line.

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the *Category* argument is used then the element should be created
       with the function ``GMP::SolverSession::CreateProgressCategory``.

    -  If the *Category* argument is not specified then this procedure will
       freeze a line in the general AIMMS progress category for displaying
       solver progress, or in the solver progress category of the generated
       mathematical program in case function
       ``GMP::Instance::CreateProgressCategory`` was called.

.. seealso::

    The procedures :aimms:func:`GMP::Instance::CreateProgressCategory`, :aimms:func:`GMP::ProgressWindow::DisplayLine`, :aimms:func:`GMP::ProgressWindow::DisplayProgramStatus`, :aimms:func:`GMP::ProgressWindow::DisplaySolverStatus`, :aimms:func:`GMP::ProgressWindow::UnfreezeLine` and
    :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
