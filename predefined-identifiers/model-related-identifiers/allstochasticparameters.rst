.. aimms:set:: AllStochasticParameters

.. _AllStochasticParameters:

AllStochasticParameters
=======================

The predefined set :aimms:set:`AllStochasticParameters` contains the names of all
parameters within an AIMMS model with the property ``Stochastic`` set.

.. code-block:: aimms

        Set AllStochasticParameters {
            SubsetOf   :  AllParameters;
            Index      :  IndexStochasticParameters;
        }

Definition
----------

    The contents of the set :aimms:set:`AllStochasticParameters` is the collection of
    all parameters with the property ``Stochastic`` set within a particular
    model.

Updatability
------------

    The contents of the set can only be modified by setting or clearing the
    property ``Stochastic`` of parameters declared in the **Model
    Explorer**.

.. seealso::

    -  Stochastic programming is discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the Language
       Reference.

    -  The intrinsic function :aimms:func:`GMP::Instance::GenerateStochasticProgram`.

    -  The sets :aimms:set:`AllParameters`, :aimms:set:`AllStochasticVariables` and :aimms:set:`AllStochasticConstraints`.

    -  Parameters are discussed in :doc:`non-procedural-language-components/parameter-declaration/parameter-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
