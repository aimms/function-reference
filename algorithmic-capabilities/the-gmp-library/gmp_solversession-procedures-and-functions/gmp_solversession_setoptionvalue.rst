.. aimms:procedure:: GMP::SolverSession::SetOptionValue(solverSession, OptionName, Value)

.. _GMP::SolverSession::SetOptionValue:

GMP::SolverSession::SetOptionValue
==================================

The procedure :aimms:func:`GMP::SolverSession::SetOptionValue` sets the value of a
solver specific option for a solver session. To a solver session
corresponds to one unique solver, and the option will only be set for
that solver.

.. code-block:: aimms

    GMP::SolverSession::SetOptionValue(
         solverSession,    ! (input) a solver session
         OptionName,       ! (input) a scalar string expression
         Value             ! (input) a scalar numeric expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

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

    -  The option value of a solver specific option can also be set in other
       ways. The value of an option belonging to a solver session is
       determined by:

       -  the procedure :aimms:func:`GMP::SolverSession::SetOptionValue` if it is
          called for the solver session, else

       -  the procedure :aimms:func:`GMP::Instance::SetOptionValue` if it is called
          for the generated mathematical program corresponding to the solver
          session, else

       -  the value used in the ``OPTION`` statement if that statement is
          used (see also :doc:`procedural-language-components/execution-statements/the-option-and-property-statements` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__), else

       -  the option value in the option tree.

    -  Options for which strings are displayed in the AIMMS **Options**
       dialog box, are also represented by numerical (integer) values. To
       obtain the corresponding option keywords, you can use the functions
       ``OptionGetString`` and ``OptionGetKeywords``.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GetOptionValue`, :aimms:func:`GMP::Instance::SetOptionValue`, :aimms:func:`GMP::SolverSession::GetOptionValue`, :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.
