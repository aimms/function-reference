.. aimms:set:: AllStochasticGenerationModes

.. _AllStochasticGenerationModes:

AllStochasticGenerationModes
============================

The predefined set :aimms:set:`AllStochasticGenerationModes` defines the modes in
which :aimms:func:`GMP::Instance::GenerateStochasticProgram` may generate a stochastic programming problem.

.. code-block:: aimms

        Set AllStochasticGenerationModes {
            Index      :  IndexStochasticGenerationModes;
            Definition :  {
                data { CreateNonAnticipativityConstraints,
                       SubstituteStochasticVariables }
            }
        }

Definition
----------

    The predefined set :aimms:set:`AllStochasticGenerationModes` defines the set of
    elements ``CreateNonAnticipativityConstraints`` and
    ``SubstituteStochasticVariables``.

Updatability
------------

    The contents of the set :aimms:set:`AllStochasticGenerationModes` cannot be
    modified.

.. seealso::

    -  Stochastic programming is discussed in Chapter 19 of the Language
       Reference.

    -  The intrinsic function :aimms:func:`GMP::Instance::GenerateStochasticProgram`.
