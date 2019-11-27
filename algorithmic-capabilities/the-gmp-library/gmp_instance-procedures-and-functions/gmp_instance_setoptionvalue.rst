.. aimms:procedure:: GMP::Instance::SetOptionValue(GMP, OptionName, Value)

.. _GMP::Instance::SetOptionValue:

GMP::Instance::SetOptionValue
=============================

| The procedure :aimms:func:`GMP::Instance::SetOptionValue` sets the value of a
  solver specific option corresponding to a generated mathematical
  program.
| This procedure can also be used to set certain Solvers General options
  (see below).

.. code-block:: aimms

    GMP::Instance::SetOptionValue(
         GMP,            ! (input) a generated mathematical program
         OptionName,     ! (input) a scalar string expression
         Value           ! (input) a scalar numeric expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *OptionName*
        A string expression holding the name of the option.

    *Value*
        A scalar numeric expression representing the new value to be assigned to
        the option.

Return Value
------------

    The procedure returns 1 if the option exists and the value can be
    assigned to the option, or 0 otherwise.

.. note::

    -  All solvers solving the generated mathematical program will use the
       option value as set by this procedure (provided that the solver
       contains the option).

    -  This procedure will be overruled by the procedure
       ``GMP::SolverSession::SetOptionValue`` in case a solver session is
       used to solve the generated mathematical program.

    -  Options for which strings are displayed in the AIMMS **Options**
       dialog box, are also represented by numerical (integer) values. To
       obtain the corresponding option keywords, you can use the functions
       ``OptionGetString`` and ``OptionGetKeywords``.

    -  This procedure can also be used to set the following Solvers General
       options:

       -  Cutoff

       -  Iteration limit

       -  Maximal number of domain errors

       -  Maximal number of integer solutions

       -  MIP absolute optimality tolerance

       -  MIP relative optimality tolerance

       -  Solver workspace

       -  Time limit

.. seealso::

    The routines :aimms:func:`GMP::Instance::GetOptionValue`, :aimms:func:`GMP::SolverSession::GetOptionValue`, :aimms:func:`GMP::SolverSession::SetOptionValue`, :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.
