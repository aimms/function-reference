.. aimms:set:: AllStochasticConstraints

.. _AllStochasticConstraints:

AllStochasticConstraints
========================

The predefined set :aimms:set:`AllStochasticConstraints` contains the names of
all constraints within an AIMMS which references in its definition a
parameter or variable with the property ``Stochastic`` set.

.. code-block:: aimms

        Set AllStochasticConstraints {
            SubsetOf   :  AllConstraints;
            Index      :  IndexStochasticConstraints;
        }

Definition
----------

    The contents of the set :aimms:set:`AllStochasticConstraints` is the collection
    of all constraints which reference a parameter or variable with the
    property ``Stochastic`` set within a particular model.

Updatability
------------

    The contents of the set can only be modified by setting or clearing the
    property ``Stochastic`` of the referenced variables and parameters in
    the definition of constraints declared in the **Model Explorer**.

.. seealso::

    -  Stochastic programming is discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the Language
       Reference.

    -  The intrinsic function :aimms:func:`GMP::Instance::GenerateStochasticProgram`.

    -  The sets :aimms:set:`AllConstraints`, :aimms:set:`AllStochasticParameters` and :aimms:set:`AllStochasticVariables`.

    -  Constraints are discussed in :doc:`optimization-modeling-components/stochastic-programming/index` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
