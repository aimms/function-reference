.. aimms:set:: AllConstraintProgrammingRowTypes

.. _AllConstraintProgrammingRowTypes:

AllConstraintProgrammingRowTypes
================================

The predefined set :aimms:set:`AllConstraintProgrammingRowTypes` contains the
collection of all possible row types available to be used by the
Constraint Programming global constraint :aimms:func:`cp::Count`.

.. code-block:: aimms

        Set AllConstraintProgrammingRowTypes {
            SubsetOf   :  AllRowTypes;
            Index      :  IndexConstraintProgrammingRowTypes;
            Definition :  data { '<=', '=', '>=', '<', '>', '<>' };
        }

Definition
----------

    The set :aimms:set:`AllConstraintProgrammingRowTypes` contains the collection of
    all possible row types available as relation operator to the function
    :aimms:func:`cp::Count`.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The function :aimms:func:`cp::Count` and the set :aimms:set:`AllRowTypes`
