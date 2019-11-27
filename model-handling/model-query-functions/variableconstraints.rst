.. aimms:function:: VariableConstraints(Variables)

.. _VariableConstraints:

VariableConstraints
===================

The function :aimms:func:`VariableConstraints` returns all the symbolic
constraints that refer to one or more variables in a given set of
variables.

.. code-block:: aimms

    VariableConstraints(
         Variables  ! (input) a subset of AllVariables
         )

Arguments
---------

    *Variables*
        The set of variables for which you want to retrieve the constraints that
        refer to them. This is a subset of :aimms:set:`AllVariables`.

.. note::

    This function operates on the compiled definition of constraints; it
    will skip inline variables during the recursion step.

Return Value
------------

    The function returns a subset of the set :aimms:set:`AllConstraints`, containing the
    constraints found.

.. seealso::

    The functions :aimms:func:`ConstraintVariables` and :aimms:func:`ReferencedIdentifiers`.
