.. aimms:set:: AllVariablesConstraints

.. _AllVariablesConstraints:

AllVariablesConstraints
=======================

The predefined set :aimms:set:`AllVariablesConstraints` contains the names of all
variables and constraints within an AIMMS model.

.. code-block:: aimms

        Set AllVariablesConstraints {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexVariablesConstraints;
        }

Definition
----------

    The contents of the set :aimms:set:`AllVariablesConstraints` is the collection of
    all *symbolic* variable and constraint names defined within a particular
    model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    variables and/or constraints in the **Model Explorer**.

.. note::

    The set :aimms:set:`AllVariablesConstraints` or subsets thereof are typically
    used in the index domain of parameters entered in the
    ``ViolationPenalties`` attribute of a ``MathematicalProgram`` declared
    within an AIMMS model.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllVariables`, :aimms:set:`AllConstraints`. The ``ViolationPenalties``
    attribute of a mathematical programs is discussed in :doc:`optimization-modeling-components/solving-mathematical-programs/infeasibility-analysis` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
