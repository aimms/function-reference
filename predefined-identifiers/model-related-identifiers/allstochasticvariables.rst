.. aimms:set:: AllStochasticVariables

.. _AllStochasticVariables:

AllStochasticVariables
======================

The predefined set :aimms:set:`AllStochasticVariables` contains the names of all
variables within an AIMMS model with the property ``Stochastic`` set.

.. code-block:: aimms

        Set AllStochasticVariables {
            SubsetOf   :  AllVariables;
            Index      :  IndexStochasticVariables;
        }

Definition
----------

    The contents of the set :aimms:set:`AllStochasticVariables` is the collection of
    all variables with the property ``Stochastic`` set within a particular
    model.

Updatability
------------

    The contents of the set can only be modified by setting or clearing the
    property ``Stochastic`` of variables declared in the **Model Explorer**.

.. seealso::

    -  Stochastic programming is discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the Language
       Reference.

    -  The intrinsic function :aimms:func:`GMP::Instance::GenerateStochasticProgram`.

    -  The sets :aimms:set:`AllVariables`, :aimms:set:`AllStochasticParameters` and :aimms:set:`AllStochasticConstraints`.

    -  Variables are discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
