.. aimms:procedure:: GMP::ProgressWindow::DeleteCategory(Category)

.. _GMP::ProgressWindow::DeleteCategory:

GMP::ProgressWindow::DeleteCategory
===================================

The procedure :aimms:func:`GMP::ProgressWindow::DeleteCategory` deletes a progress
category.

.. code-block:: aimms

    GMP::ProgressWindow::DeleteCategory(
         Category          ! (input) a progress category
         )

Arguments
---------

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::CreateProgressCategory` and :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
