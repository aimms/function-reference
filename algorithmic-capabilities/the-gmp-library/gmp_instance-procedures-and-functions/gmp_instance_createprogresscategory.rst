.. aimms:function:: GMP::Instance::CreateProgressCategory(GMP, Name)

.. _GMP::Instance::CreateProgressCategory:

GMP::Instance::CreateProgressCategory
=====================================

The function :aimms:func:`GMP::Instance::CreateProgressCategory` creates a new GMP
progress category for a generated mathematical program. This progress
category can be used to display GMP related information in the progress
window.

.. code-block:: aimms

    GMP::Instance::CreateProgressCategory(
         GMP,              ! (input) a generated mathematical program
         [Name]            ! (input, optional) a string expression
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *Name*
        A string that holds the name of the progress category.

Return Value
------------

    The function returns an element in the set :aimms:set:`AllProgressCategories`.

.. note::

    -  If no progress category is specified for the generated mathematical
       program then the GMP progress will be displayed in the general AIMMS
       progress category for GMP progress. This general AIMMS progress
       category will be used by all generated mathematical programs for
       which no progress category is specified. (Progress information for a
       normal solve is always displayed in the general AIMMS progress
       category.)

    -  After calling :aimms:func:`GMP::Instance::CreateProgressCategory` solver
       progress will by default be displayed in the solver progress category
       of the generated mathematical program, and no longer in the general
       AIMMS progress category for solver progress.

    -  If the *Name* argument is not specified then the name of the
       generated mathematical program will be used to name the element in
       the set ``AllProgressCategories``.

    -  The information displayed in a GMP progress category is controlled by
       AIMMS and cannot be modified by the user.

    -  A progress category created before for the generated mathematical
       program will be deleted.

.. seealso::

    The routines :aimms:func:`GMP::ProgressWindow::DeleteCategory` and :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
