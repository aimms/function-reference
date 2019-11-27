.. aimms:set:: AllStochasticScenarios

.. _AllStochasticScenarios:

AllStochasticScenarios
======================

The predefined set :aimms:set:`AllStochasticScenarios` contains the names of all
stochastic scenarios.

.. code-block:: aimms

        Set AllStochasticScenarios {
            Index       :  IndexStochasticScenarios;
        }

Definition
----------

    The contents of the set :aimms:set:`AllStochasticScenarios` is the collection of
    all stochastic scenarios.

Updatability
------------

    The contents of the set can be modified in the model.

.. seealso::

    -  Stochastic programming is discussed in Chapter 19 of the Language
       Reference.

    -  The intrinsic function :aimms:func:`GMP::Instance::GenerateStochasticProgram`.
