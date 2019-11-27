.. aimms:function:: GMP::Instance::GetOptionValue(GMP, OptionName)

.. _GMP::Instance::GetOptionValue:

GMP::Instance::GetOptionValue
=============================

| The function :aimms:func:`GMP::Instance::GetOptionValue` returns the value of a
  solver specific option corresponding to a generated mathematical
  program as set with the procedure ``GMP::Instance::SetOptionValue``.
| This procedure can also be used to retrieve the current option value
  of certain Solvers General options (see below).

.. code-block:: aimms

    GMP::Instance::GetOptionValue(
         GMP,            ! (input) a generated mathematical program
         OptionName      ! (input) a scalar string expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *OptionName*
        A string expression holding the name of the option.

Return Value
------------

    In case of success, the function returns the current option value.
    Otherwise it returns ``UNDF``.

.. note::

    -  If the procedure ``GMP::Instance::SetOptionValue`` has not been
       called then this function will fail and return ``UNDF`` (unless the
       option is a Solvers General option).

    -  Options for which strings are displayed in the AIMMS **Options**
       dialog box, are also represented by numerical (integer) values. To
       obtain the corresponding option keywords, you can use the functions
       ``OptionGetString`` and ``OptionGetKeywords``.

    -  This procedure can also be used to retrieve the current option value
       of the following Solvers General options:

       -  Cutoff

       -  Iteration limit

       -  Maximal number of domain errors

       -  Maximal number of integer solutions

       -  MIP absolute optimality tolerance

       -  MIP relative optimality tolerance

       -  Solver workspace

       -  Time limit

.. seealso::

    The routines :aimms:func:`GMP::Instance::SetOptionValue`, :aimms:func:`GMP::SolverSession::GetOptionValue`, :aimms:func:`GMP::SolverSession::SetOptionValue`, :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.
