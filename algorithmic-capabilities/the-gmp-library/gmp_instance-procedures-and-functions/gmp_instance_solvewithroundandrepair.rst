.. aimms:procedure:: GMP::Instance::SolveWithRoundAndRepair(GMP, variableSet, freq, fixIndices, slackVars)

.. _GMP::Instance::SolveWithRoundAndRepair:

GMP::Instance::SolveWithRoundAndRepair
======================================

| The procedure :aimms:func:`GMP::Instance::SolveWithRoundAndRepair` solves a
  generated mathematical program of type MIP or MIQP, using a round-and-repair
  heuristic to find good integer solutions faster.
|
| While the solver works on the MIP, the procedure collects fractional (node LP)
  solutions and interrupts the solve after every *freq* distinct fractional
  solutions. The binary variables in *variableSet* are then rounded, and the
  rounded values are used to construct an integer solution by solving two
  auxiliary MIPs.
|
| The repaired solution is passed to the solver as a heuristic solution, and the
  solve continues. This is repeated until the relative MIP gap of the
  generated mathematical program is reached, or the time limit expires.

.. code-block:: aimms

    GMP::Instance::SolveWithRoundAndRepair(
         GMP,            ! (input) a generated mathematical program
         variableSet,    ! (input) a set of binary variables
         [freq],         ! (input, optional, default 3) a scalar integer value
         [fixIndices],   ! (input, optional, default "") a string expression
         [slackVars]     ! (input, optional) a set of variables
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *variableSet*
        A subset of :aimms:set:`AllIntegerVariables`, containing the binary
        variables that are rounded. It should contain at least one variable, and
        all its variables should be binary.

    *freq*
        A positive integer scalar value: the number of distinct fractional
        solutions after which the solve is interrupted to round and repair. The
        default is 3.

    *fixIndices*
        A string of the form ``"var:idx[,idx...][;var:idx[,idx...]...]"``. For
        each variable *var* of *variableSet* in it, the columns of the variable are
        grouped by the indices *idx*. If all fractional values in a group are
        (almost) 0, or all are (almost) 1, then all columns in the group are fixed
        at that value in the first repair MIP. Here, (almost) 0 means smaller than
        0.01, and (almost) 1 means larger than 0.99. Values of variables frozen
        via the ``.NonvarStatus`` suffix are included in this test. The default is
        the empty string, meaning that no columns are grouped.

    *slackVars*
        A subset of :aimms:set:`AllVariables` that has no variables in common with
        *variableSet*. The variables in *slackVars* are fixed at their values in
        the fractional solution in the first repair MIP. If omitted, no
        variables are fixed this way.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure can only be used for models of type MIP or MIQP, and
       only with a solver that supports interrupting a solve and continuing it
       later, which are CPLEX and Gurobi. See the article `Implementing Continued
       Solves <https://how-to.aimms.com/Articles/685/685-continued-solve.html>`__
       for more information about continued solves.

    -  Like :aimms:func:`GMP::Instance::Solve`, this procedure copies the initial
       solution from the model identifiers, and stores the final solution back
       in the model identifiers.

    -  The procedure installs its own heuristic callback. It fails if a heuristic
       callback procedure has already been installed with
       :aimms:func:`GMP::Instance::SetCallbackHeuristic`, or if an asynchronous
       solve of the generated mathematical program is running.

    -  The time limit of the generated mathematical program (option ``Time
       Limit``) applies to the whole procedure, including the solves of the
       repair MIPs. If the time limit expires, the solver status becomes
       ``ResourceInterrupt``.

    -  If the first repair MIP is infeasible, the generated mathematical
       program is infeasible as well, and its program status becomes
       ``Infeasible``.

    -  In *fixIndices*, the name of a variable or index that is declared in a
       library can be given without its library prefix.

    -  The procedure uses solutions 2 to 5 in the solution repository of the
       generated mathematical program, overwriting any solutions stored there.

Example
-------

Assume that ``MP`` is a mathematical program containing the binary variable
``UnitOn(u,h)``, which states whether unit ``u`` is committed in hour ``h``, and
the slack variable ``DemandSlack(h)``. We declare the following identifiers (in
ams format):

.. code-block:: aimms

    ElementParameter myGMP {
        Range: AllGeneratedMathematicalPrograms;
    }
    Set RoundingVariables {
        SubsetOf: AllIntegerVariables;
    }
    Set SlackVariables {
        SubsetOf: AllVariables;
    }

To solve ``MP`` with the round-and-repair heuristic, where all hours of a unit are
fixed in the first repair MIP if the fractional values of that unit are (almost)
0 for all hours, or (almost) 1 for all hours, we could use:

.. code-block:: aimms

    myGMP := GMP::Instance::Generate(MP);

    RoundingVariables := data { UnitOn };
    SlackVariables := data { DemandSlack };

    GMP::Instance::SolveWithRoundAndRepair( myGMP, RoundingVariables,
        fixIndices: "UnitOn:u", slackVars: SlackVariables );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Instance::SetCallbackHeuristic` and :aimms:func:`GMP::Instance::SetTimeLimit`.
