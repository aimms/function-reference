.. aimms:procedure:: GMP::ProgressWindow::UnfreezeLine(lineNo, Category)

.. _GMP::ProgressWindow::UnfreezeLine:

GMP::ProgressWindow::UnfreezeLine
=================================

The procedure :aimms:func:`GMP::ProgressWindow::UnfreezeLine` unlocks a frozen
line in the Progress Window.

.. code-block:: aimms

    GMP::ProgressWindow::UnfreezeLine(
         lineNo,           ! (input) a line number
         [Category]        ! (optional) a progress category
         )

Arguments
---------

    *lineNo*
        The number of the line that should be freed.

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the *Category* argument is used then the element should be created
       with the function ``GMP::SolverSession::CreateProgressCategory``.

    -  If the *Category* argument is not specified then this procedure will
       unfreeze a line in the general AIMMS progress category for displaying
       solver progress, or in the solver progress category of the generated
       mathematical program in case function
       ``GMP::Instance::CreateProgressCategory`` was called.

.. seealso::

    The procedures :aimms:func:`GMP::Instance::CreateProgressCategory`, :aimms:func:`GMP::ProgressWindow::DisplayLine`, :aimms:func:`GMP::ProgressWindow::FreezeLine` and :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
