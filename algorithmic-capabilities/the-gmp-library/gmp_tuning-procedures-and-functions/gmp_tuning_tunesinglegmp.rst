.. aimms:procedure:: GMP::Tuning::TuneSingleGMP(GMP, FixedOptions, ApplyTunedSettings, OptionFileName)

.. _GMP::Tuning::TuneSingleGMP:

GMP::Tuning::TuneSingleGMP
==========================

The procedure :aimms:func:`GMP::Tuning::TuneSingleGMP` tunes the solver options
for a generated mathematical program.

.. code-block:: aimms

    GMP::Tuning::TuneSingleGMP(
         GMP,                  ! (input) generated mathematical program
         FixedOptions,         ! (input) set expression
         [ApplyTunedSettings], ! (optional) scalar numerical expression
         [OptionFileName]      ! (optional) scalar string expression
    )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

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

    -  This procedure does not return a solution for the GMP and therefore
       the model identifiers are not changed.

    -  The tuned options will be written to the listing file.

    -  The options file (if any) can be imported into the AIMMS project
       using the options dialog box.

    -  This procedure is only supported by CPLEX and GUROBI.

Example
-------

    Assume that 'MP' is a mathematical program and 'gmpMP' an element
    parameter with range 'AllGeneratedMathematicalPrograms'. Furthermore, we
    have a set 'FixedOptions' defined as: 

    .. code-block:: aimms

               Set FixedOptions {
                   SubsetOf   :  AllOptions;
                   Definition :  data { 'CPLEX 12.9::mip_search_strategy' };
               }

    To tune 'MP' we have
    to run: 

    .. code-block:: aimms

               gmpMP := GMP::Instance::Generate( MP );

               GMP::Tuning::TuneSingleGMP( gmpMP, FixedOptions );

    Here the opion 'mip search strategy' is fixed and
    will not be tuned (assuming we are using solver CPLEX 12.9).

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Tuning::SolveSingleMPS` and :aimms:func:`GMP::Tuning::TuneMultipleMPS`.
