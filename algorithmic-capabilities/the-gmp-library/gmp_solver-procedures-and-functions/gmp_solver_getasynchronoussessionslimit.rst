.. aimms:function:: GMP::Solver::GetAsynchronousSessionsLimit(solver, cores, GMP)

.. _GMP::Solver::GetAsynchronousSessionsLimit:

GMP::Solver::GetAsynchronousSessionsLimit
=========================================

The function :aimms:func:`GMP::Solver::GetAsynchronousSessionsLimit` returns the
maximum number of asynchronous solver sessions that can run simultaneous
for a certain solver. This number depends on the AIMMS license.

.. code-block:: aimms

    GMP::Solver::GetAsynchronousSessionsLimit(
         solver,     ! (input) a solver
         [cores],    ! (input, optional) a binary scalar value
         [GMP]       ! (input, optional) a generated mathematical program
         )

Arguments
---------

    *solver*
        An element in the set :aimms:set:`AllSolvers`.

    *cores*
        A binary scalar indicating whether the this function should take into
        account the number of cores on the machine. The default is 0 (cores are
        not used).

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`. By default this argument is empty.

Return Value
------------

    The maximal number of asynchronous solver sessions that can run
    simultaneous using *solver*, or any other version of the same solver. If
    the *cores* argument equals 1 then this function returns the number of
    cores on the machine if that number is smaller than the maximal number
    of asynchronous solver sessions. If the *GMP* argument is used then this
    function will return 0 if the specified generated mathematical program
    cannot be used for asynchronous executing (e.g., if it contains a
    constraint with a nonlinear expression referencing an external
    function).

.. note::

    -  The function returns 0 if the solver cannot be found or is not
       licensed. It also returns 0 if the solver cannot be used to do an
       asynchronous solve (e.g., BARON, CBC, ODH-CPLEX).

    -  The function returns 1 if the solver is not thread-safe (e.g., IPOPT,
       SNOPT.

    -  To count the number of asynchronous solver sessions currently running
       with a solver, AIMMS checks all solver versions available. For
       example, if one asynchronous solver session is running with
       CPLEX 12.9 and another simultaneous with CPLEX 12.8 then solver CPLEX
       is running two asynchronous solver sessions. The value returned by
       this function limits all solver versions together (even though the
       argument passed to the function refers to a particular solver
       version).

Example
-------

    Assume that 'MaxSes' is a parameter then the following statement returns
    the maximal number of asynchronous solver sessions for CPLEX:

    .. code-block:: aimms

               MaxSes := GMP::Solver::GetAsynchronousSessionsLimit( 'CPLEX 12.9' );

    The value MaxSes is the limit on asynchronous solver
    sessions that can run at the same time with CPLEX 12.9 plus CPLEX 12.8
    plus CPLEX 12.7, etc.

.. seealso::

    The routine :aimms:func:`GMP::SolverSession::AsynchronousExecute`.
