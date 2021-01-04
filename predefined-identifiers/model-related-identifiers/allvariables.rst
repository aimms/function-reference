.. aimms:set:: AllVariables

.. _AllVariables:

AllVariables
============

The predefined set :aimms:set:`AllVariables` contains the names of all variables
within an AIMMS model.

.. code-block:: aimms

        Set AllVariables {
            SubsetOf   :  AllVariablesConstraints;
            Index      :  IndexVariables;
        }

Definition
----------

    The contents of the set :aimms:set:`AllVariables` is the collection of all
    *symbolic* variable names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    variables in the **Model Explorer**.

.. note::

    The set :aimms:set:`AllVariables` or subsets thereof are typically used in the
    ``Variables`` attribute of ``MathematicalPrograms`` declared within an
    AIMMS model.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllConstraints`. Variables are discussed in :doc:`optimization-modeling-components/variable-and-constraint-declaration/variable-declaration-and-attributes`,
    mathematical programs in :doc:`optimization-modeling-components/solving-mathematical-programs/mathematicalprogram-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
