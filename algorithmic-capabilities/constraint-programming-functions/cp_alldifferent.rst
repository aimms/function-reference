.. aimms:function:: cp::AllDifferent(valueBinding, values)

.. _cp::AllDifferent:

cp::AllDifferent
================

This function enforces (a slice of) an indexed variable or expression to
be *assigned* all different values, or to *determine* whether (a slice
of) an indexed identifier or expression contains all different values.

Mathematical Formulation
------------------------

    The function ``cp::AllDifferent(i,x_i)`` is equivalent to

    .. math:: \forall i, j, i\neq j: x_i \neq x_j

Function Prototype
------------------

    .. code-block:: aimms

        cp::AllDifferent(
                valueBinding, ! (input) an index binding
                values        ! (input/output) an expression
        )

Arguments
---------

    *valueBinding*
        The index binding for which the ``values`` argument should have all
        different values.

    *values*
        The expression that should have a different value for each element in
        ``valueBinding``. This expression may involve variables, but can only
        contain integral or element values (i.e. no strings, fractional, or unit
        values).

Return Value
------------

    This function returns 1 if the values in ``values`` are all distinct, or
    0 otherwise. If ``valueBinding`` results in zero or one element, then
    this function will also return 1, and may issue a warning on non-binding
    constraints.

.. note::

    The following two constraints are equivalent, but a constraint
    programming solver handles the single row instantiated by
    ``Enforcevalues1`` much more efficiently than the many instantiated rows
    resulting from ``Enforcevalues2``. 

    .. code-block:: aimms

                Constraint Enforcevalues1 {
                    Definition   :  cp::AllDifferent( i, x(i) );
                }

    .. code-block:: aimms

                Constraint Enforcevalues2 {
                    IndexDomain  :  (i,j) | i < j;
                    Definition   :  x(i) <> x(j);
                }

Example
-------

    .. code-block:: aimms

                ElementParameter TheElementParameter {
                    IndexDomain  : i
                    Definition   : {
                        data{ 1 : A,
                              2 : B,
                              3 : C }
                    }
                }

    With the above data,
    ``cp::AllDifferent(i, TheElementParameter(i))`` returns 1, because all
    elements are different. However, with the data below, it returns 0 (the
    element 'A' appears twice). 

    .. code-block:: aimms

                ElementParameter TheElementParameter {
                    IndexDomain  : i;
                    Definition   : {
                        data{ 1 : A,
                              2 : B,
                              3 : C }
                    }
                }

    The following code snippet is
    extracted from the Sudoku example (in which all rows, columns and blocks
    should have different values). It illustrates the selection of values;
    particularly illustrating the use of an index domain condition on the
    first argument as used in the definition of ``DifferentValuesPerBlock``.

    .. code-block:: aimms

                Constraint DifferentValuesPerRow {
                    IndexDomain  :  i;
                    Definition   :  cp::AllDifferent( j, x(i,j) );
                }
                Constraint DifferentValuesPerColumn {
                    IndexDomain  :  j;
                    Definition   :  cp::AllDifferent( i, x(i,j) );
                }
                Constraint DifferentValuesPerBlock {
                    IndexDomain  :  k;
                    Definition   :  cp::AllDifferent( (i,j) | Blck(i,j) = k, x(i,j) );
                }

.. seealso::

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  Further information on index binding can be found in the Chapter on
       Index Binding 9 in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The global constraint catalog
       http://www.emn.fr/z-info/sdemasse/gccat/Calldifferent.html which
       references this function as ``alldifferent``.
