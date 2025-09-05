.. aimms:procedure:: GMP::Tuning::TuneMultipleMPS(DirectoryName, Solver, FixedOptions, ApplyTunedSettings, OptionFileName)

.. _GMP::Tuning::TuneMultipleMPS:

GMP::Tuning::TuneMultipleMPS
============================

The procedure :aimms:func:`GMP::Tuning::TuneMultipleMPS` tunes the solver options
for a set of problems represented by MPS, LP or SAV files.

.. code-block:: aimms

    GMP::Tuning::TuneMultipleMPS(
         DirectoryName,        ! (input) scalar string expression
         Solver,               ! (input) scalar element parameter
         FixedOptions,         ! (input) set expression
         [ApplyTunedSettings], ! (optional) scalar numerical expression
         [OptionFileName]      ! (optional) scalar string expression
    )

Arguments
---------

    *DirectoryName*
        The name of the directory containing the problems to be tuned. All
        problems with file format ``.mps``, ``.lp`` or ``.sav`` inside the directory
        will be used.

    *Solver*
        An element in the set :aimms:set:`AllSolvers`.

    *FixedOptions*
        A subset of the predefined set :aimms:set:`AllOptions`, containing the set of all
        solver options that should *not* be tuned by the solver. For fixed
        options the current AIMMS project settings are used.

    *ApplyTunedSettings*
        A 0-1 value indicating whether the tuned option settings should be used
        inside the project immediately. The default is 0.

    *OptionFileName*
        The name of the options file to which the tuned options will be written.
        If this argument is not specified then no options file will be created.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  All solver options not in the set *FixedOptions* will be subject to
       tuning even if such an option is set to a non-default value inside
       the AIMMS project.

    -  Mixed problem sets are not supported, i.e., you cannot mix LP
       problems with MIP problems.

    -  The tuned options will be written to the listing file.

    -  The options file (if any) can be imported into the AIMMS project
       using the options dialog box.

    -  This procedure is only supported by CPLEX and Gurobi.

    -  Only CPLEX supports the SAV format.

Example
-------

Assume we have a set ``FixedOptions`` defined as: 

.. code-block:: aimms

    Set FixedOptions {
        SubsetOf   :  AllOptions;
        Definition :  data { 'CPLEX 12.10::mip_search_strategy' };
    }

Using CPLEX 12.10 we tune all ``.mps``, ``.lp`` and ``.sav`` problems inside the
directory ``Set1`` by executing: 

.. code-block:: aimms

            GMP::Tuning::TuneMultipleMPS( "Set1", 'CPLEX 12.10', FixedOptions );

Note that the option ``mip search strategy`` is fixed and will not be tuned.

.. seealso::

    - The routines :aimms:func:`GMP::Tuning::SolveSingleMPS` and :aimms:func:`GMP::Tuning::TuneSingleGMP`.
