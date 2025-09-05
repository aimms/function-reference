.. aimms:function:: GMP::SolverSession::GetOptionValue(solverSession, OptionName)

.. _GMP::SolverSession::GetOptionValue:

GMP::SolverSession::GetOptionValue
==================================

The function :aimms:func:`GMP::SolverSession::GetOptionValue` returns the value of
a solver specific option for a solver session.

.. code-block:: aimms

    GMP::SolverSession::GetOptionValue(
         solverSession,    ! (input) a solver session
         OptionName        ! (input) a scalar string expression
         )

Arguments
---------

    *solverSession*
        An element in the set :aimms:set:`AllSolverSessions`.

    *OptionName*
        A string expression holding the name of the option.

Return Value
------------

    In case of success, the function returns the current option value.
    Otherwise it returns ``UNDF``.

.. note::

    Options for which strings are displayed in the AIMMS **Options** dialog
    box, are also represented by numerical (integer) values. To obtain the
    corresponding option keywords, you can use the functions
    ``OptionGetString`` and ``OptionGetKeywords``.

.. seealso::

    -  The routines :aimms:func:`GMP::Instance::GetOptionValue`, :aimms:func:`GMP::Instance::SetOptionValue`, :aimms:func:`GMP::SolverSession::SetOptionValue`, :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.
