.. aimms:procedure:: GMP::ProgressWindow::Transfer(Category, solverSession)

.. _GMP::ProgressWindow::Transfer:

GMP::ProgressWindow::Transfer
=============================

The procedure :aimms:func:`GMP::ProgressWindow::Transfer` transfers a progress
category that was created for a solver session to another solver
session. This procedure allows you to share a progress category among
several solver sessions.

.. code-block:: aimms

    GMP::ProgressWindow::Transfer(
         Category,         ! (input) a progress category
         solverSession     ! (input) a solver session
         )

Arguments
---------

    *Category*
        An element in the set :aimms:set:`AllProgressCategories`.

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *Category* should have been created with the function
       :aimms:func:`GMP::SolverSession::CreateProgressCategory`.

    -  The *solverSession* argument specifies the solver session to which
       the progress category should be transfered.

Example
-------

    In the example below we create two GMPs and for each GMP a solver
    session. Next we create a progress category for the first solver
    session. After executing the first solver session we transfer the
    progress category to the second solver session. By transfering the
    progress category we ensure that both solver sessions use the same area
    in the progress window. 

    .. code-block:: aimms

               myGMP1 := GMP::Instance::Generated( MP1 );
               session1 := GMP::Instance::CreateSolverSession( myGMP1 );

               myGMP2 := GMP::Instance::Generated( MP2 );
               session2 := GMP::Instance::CreateSolverSession( myGMP2 );

               pc := GMP::SolverSession::CreateProgressCategory( session1 );

               GMP::SolverSession::Execute( session1 );

               GMP::ProgressWindow::Transfer( pc, session2 );

               GMP::SolverSession::Execute( session2 );

.. seealso::

    The procedure :aimms:func:`GMP::SolverSession::CreateProgressCategory`.
