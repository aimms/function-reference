.. aimms:function:: GMP::Stochastic::CreateBendersRootproblem(GMP, name)

.. _GMP::Stochastic::CreateBendersRootproblem:

GMP::Stochastic::CreateBendersRootproblem
=========================================

| The function :aimms:func:`GMP::Stochastic::CreateBendersRootproblem` generates a
  mathematical program that represents the Benders problem at the unique
  node at stage 1 in the scenario tree of a stochastic mathematical
  program, and it also creates all Benders problems for all other nodes.
| This function collects all columns and rows that correspond to the
  unique (representive) scenario at stage 1 in the scenario tree.

.. code-block:: aimms

    GMP::Stochastic::CreateBendersRootproblem(
         GMP,               ! (input) a generated mathematical program
         [name]             ! (optional) a string expression
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that holds the name for the Benders problem created for *GMP*
        at stage 1.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms` with the name as specified by the
    *name* argument.

.. note::

    -  The *GMP* should have been created by the function
       ``GMP::Instance::GenerateStochasticProgram``.

    -  The generated math program belonging to the node of a Benders
       subproblem can be obtained by using the function
       ``GMP::Stochastic::BendersFindReference``.

    -  If the *name* argument is not specified, or if it is the empty
       string, then the name of the *GMP*, stage 1 and the unique
       representive scenario at stage 1 are used to create a new element in
       the set :aimms:set:`AllGeneratedMathematicalPrograms`.

.. seealso::

    The routines :aimms:func:`GMP::Instance::GenerateStochasticProgram`, :aimms:func:`GMP::Stochastic::BendersFindReference` and :aimms:func:`GMP::Stochastic::UpdateBendersSubproblem`. See Section 19.1 of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__ for more details on scenario tree, scenarios and
    stages.
