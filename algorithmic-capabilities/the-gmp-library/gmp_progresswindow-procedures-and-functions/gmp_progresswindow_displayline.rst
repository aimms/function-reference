.. aimms:procedure:: GMP::ProgressWindow::DisplayLine(lineNo, title, value, Category)

.. _GMP::ProgressWindow::DisplayLine:

GMP::ProgressWindow::DisplayLine
================================

The procedure :aimms:func:`GMP::ProgressWindow::DisplayLine` writes one line with
progress information in the Progress Window. The *lineNo* argument gives
the number of the line in which the information has to be shown. The
title contains a string that will be displayed on the left side of the
line; the value will be displayed on the right side.

.. code-block:: aimms

    GMP::ProgressWindow::DisplayLine(
         lineNo,           ! (input) a line number
         title,            ! (input) a title
         value,            ! (input) a value
         [Category]        ! (optional) a progress category
         )

Arguments
---------

    *lineNo*
        The number of the line in which the information has to be shown. Its
        value should be a number between 1 and the maximum number of lines
        available in the Progress Window (currently 6).

    *title*
        The string that will be displayed on the left side of the line.

    *value*
        The value that will be displayed on the right side of the line.

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the *Category* argument is used then the element should be created
       with the function :aimms:func:`GMP::SolverSession::CreateProgressCategory`.

    -  To freeze (lock) a line the procedure
       :aimms:func:`GMP::ProgressWindow::FreezeLine` should be called. To unfreeze it
       thereafter the procedure :aimms:func:`GMP::ProgressWindow::UnfreezeLine` should
       be called.

.. seealso::

    The routines :aimms:func:`GMP::ProgressWindow::DisplaySolverStatus`, :aimms:func:`GMP::ProgressWindow::DisplayProgramStatus`, :aimms:func:`GMP::ProgressWindow::DisplaySolver`, :aimms:func:`GMP::ProgressWindow::FreezeLine`, :aimms:func:`GMP::ProgressWindow::UnfreezeLine` and
    :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
