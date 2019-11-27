.. aimms:function:: cp::Count(inspectedBinding, inspectedValues, lookupValue, relationalOperator, occurrenceLimit)

.. _cp::Count:

cp::Count
=========

The function :aimms:func:`cp::Count` can be used to restrict the number of
occurrences of a particular value in (a slice of) an indexed identifier
or expression. This function is typically used in constraints that
enforce a selected value a limited number of times.

Mathematical Formulation
------------------------

    The function ``cp::Count(i,x_i,c,\otimes,y)`` returns 1 if the number of
    occurrences of :math:`x_i` equal to the value :math:`c`, is related to
    :math:`y` according to the relational operator :math:`\otimes`. The
    function ``cp::Count(i,x_i,c,\otimes,y)`` is equivalent to

    .. math:: \begin{array}{l} \sum_{i} (x_i=c) \otimes y \\ \otimes \in \{ \leq, =, \geq, <, >, \neq \} \end{array}

Function Prototype
------------------

    .. code-block:: aimms

            cp::Count(
                inspectedBinding,   ! (input) an index binding
                inspectedValues,    ! (input/output) an expression
                lookupValue,        ! (input) an expression
                relationalOperator, ! (input) an element  
                occurrenceLimit     ! (input/output) an expression 
            )

Arguments
---------

    *inspectedBinding*
        The index binding that specifies, together with the ``inspectedValues``
        argument, the set of values in which the ``lookupValue`` should be
        counted.

    *inspectedValues*
        The expression indexed over ``inspectedBinding`` for which the number of
        occurrences of the value ``lookupValue`` is counted. This expression may
        involve variables, but can only contain integer or element values
        (i.e. no strings, fractional or unit values).

    *lookupValue*
        The particular value for which the number of occurrences in
        ``inspectedValues`` should be counted. This expression cannot involve
        variables. The data type should match the data type of
        ``inspectedValues``.

    *relationalOperator*
        The relational operator that indicates how the number of occurrences is
        limited to the ``occurrenceLimit`` argument. This can be an expression
        and should result in an element in the set :aimms:set:`AllConstraintProgrammingRowTypes`. This expression
        cannot involve variables.

    *occurrenceLimit*
        The number of occurrences of ``lookupValue`` is limited to the
        ``occurrenceLimit``. This can be an expression that may involve
        variables.

Return Value
------------

    This function returns 1 if the number of occurences of ``lookupValue``
    does not exceed the ``occurenceLimit`` argument according to the
    ``relationalOperator``. In all other cases, the function returns 0.

Example
-------

    .. code-block:: aimms

                ElementParameter TheElementParameter {
                    IndexDomain  :  i;
                    Definition   :  data{ 1 : A, 2 : B, 3 : A };
                }

    With the above data, the following holds: 

    .. code-block:: aimms

            cp::Count(i, TheElementParameter(i), 'B', '<=', 1) = 1
            cp::Count(i, TheElementParameter(i), 'B', '<', 1) = 0
            cp::Count(i, TheElementParameter(i), 'A', '=', 2) = 1

    The
    following constraint sets the number of stores supplied by a warehouse
    ``w`` equal to the variable ``warehouseUsage``: 

    .. code-block:: aimms

                Set Warehouses {
                    Index        :  w;
                }
                Set Suppliers {
                    Index        :  s;
                }
                ElementParamter SupplyingWarehouse {
                    IndexDomain  :  s;
                    Range        :  Warehouses;
                }
                Variable WarehouseUsage {
                    IndexDomain  :  w;
                    Range        :  integer;
                }
                Constraint CountUsedWarehouses {
                    IndexDomain  :  w;
                    Definition   : {
                        cp::count( s, supplyingWarehouse(s), w,
                                  '=', warehouseUsage(w) )
                    }
               }

.. seealso::

    -  The functions :aimms:func:`cp::Cardinality` and :aimms:func:`cp::Sequence`.

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The global constraint catalog
       http://www.emn.fr/z-info/sdemasse/gccat/Ccount.html which references
       this function as ``count``, or, depending on a particular choice of
       :math:`\otimes`, as ``atleast``, ``atmost`` or ``exactly``.
