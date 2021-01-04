.. aimms:set:: AllConstraints

.. _AllConstraints:

AllConstraints
==============

The predefined set :aimms:set:`AllConstraints` contains the names of all
constraints within an AIMMS model.

.. code-block:: aimms

        Set AllConstraints {
            SubsetOf   :  AllVariablesConstraints;
            Index      :  IndexConstraints;
        }

Definition
----------

    The contents of the set :aimms:set:`AllConstraints` is the collection of all
    *symbolic* constraint names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    constraints in the **Model Explorer**.

.. note::

    The set :aimms:set:`AllConstraints` or subsets thereof are typically used in the
    ``Constraints`` attribute of ``MathematicalProgram`` declared within an
    AIMMS model.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllVariables`. Constraints are discussed in :doc:`optimization-modeling-components/variable-and-constraint-declaration/constraint-declaration-and-attributes`, 
    mathematical programs in :doc:`optimization-modeling-components/solving-mathematical-programs/mathematicalprogram-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
