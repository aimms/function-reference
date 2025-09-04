.. aimms:function:: ConstraintVariables(Contraints)

.. _ConstraintVariables:

ConstraintVariables
===================

The function :aimms:func:`ConstraintVariables` returns all the symbolic variables
that are referred in a certain collection of constraints, including the
variables that are referred in the definitions of these variables.

.. code-block:: aimms

    ConstraintVariables(
         Contraints      ! (input) a subset of AllConstraints
         )

Arguments
---------

    *Contraints*
        The set of constraints for which you want to retrieve the referred
        variables.

    .. note::

        This function operates on the compiled definition of constraints; it
        will skip inline variables.

Example
-------

.. code-block:: aimms

    Model Main_cv {
        Variable x {
            Range: free;
        }
        Variable y {
            Range: free;
        }
        Variable z {
            Range: free;
            Property: Inline;
            Definition: x + y;
        }
        Constraint c {
            Definition: z > 0;
        }
        Set S {
            SubsetOf: AllConstraints;
            Index: i;
            Definition: data { c };
        }
        Set T {
            SubsetOf: AllVariables;
            Index: j;
        }
        Set U {
            SubsetOf: AllVariables;
            Index: k;
        }
        Set setje {
            Index: ii;
            Definition: data { a, b };
        }
        Parameter P {
            IndexDomain: ii;
            Definition: data { a : 3,  b : 4 };
        }
        ElementParameter colPar {
            IndexDomain: ii;
            Range: AllColors;
            Definition: data { a : red,  b : yellow };
        }
        Procedure MainInitialization;
        Procedure MainExecution {
            Body: {
                T := ConstraintVariables( S );
                U := ReferencedIdentifiers( S, AllAttributeNames, recursive: 1 );
                display T, U ;
            }
        }
        Procedure MainTermination {
            Body: {
                return 1 ;
            }
        }
    }

Running ``MainExecution`` will create the following listing
file: 

.. code-block:: aimms

    T := data { x, y } ;

    U := data { x, y, z } ;

Because ``z`` is an inline variable.

Return Value
------------

    The function returns a subset of the set :aimms:set:`AllVariables`, containing the
    variables found.

.. seealso::

    - The function :aimms:func:`VariableConstraints` and :aimms:func:`ReferencedIdentifiers`.
