.. aimms:set:: AllProgressCategories

.. _AllProgressCategories:

AllProgressCategories
=====================

The predefined set :aimms:set:`AllProgressCategories` contains the names of all
created progress categories.

.. code-block:: aimms

        Set AllProgressCategories {
            Index       :  IndexProgressCategories;
        }

Definition
----------

    The contents of the set :aimms:set:`AllProgressCategories` is the collection of
    all progress categories created by the functions :aimms:func:`GMP::Instance::CreateProgressCategory` and
    :aimms:func:`GMP::SolverSession::CreateProgressCategory`. These progress categories are used by the
    ``GMP::ProgressWindow`` functions.

Updatability
------------

    The contents of the set can only be modified through the functions
    :aimms:func:`GMP::Instance::CreateProgressCategory`, :aimms:func:`GMP::SolverSession::CreateProgressCategory` and :aimms:func:`GMP::ProgressWindow::DeleteCategory`.
