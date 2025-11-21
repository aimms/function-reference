.. aimms:function:: GMP::Instance::GetAttributeValue(GMP, attr, objNo)

.. _GMP::Instance::GetAttributeValue:

GMP::Instance::GetAttributeValue
================================

The function :aimms:func:`GMP::Instance::GetAttributeValue` can be used to get the value
of certain solver attributes, related to solving a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetAttributeValue(
         GMP,            ! (input) a generated mathematical program
         attr,           ! (input) a string expression
         [objNo]         ! (input, optional) an integer expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *attr*
        A string that holds the name of the attribute.

    *objNo*
        A nonnegative scalar value specifying the objective number in a
        multi-objective optimization problem. The default value is 0.

Return Value
------------

    In case of success, the function returns the attribute value. Otherwise it returns ``UNDF``.

.. note::

    -  The attribute name is case-insensitive.

    -  This function is only supported by CPLEX and Gurobi.

    -  This function cannot be called inside a callback procedure.

Attributes
~~~~~~~~~~

| The table below shows the model attributes supported by CPLEX and Gurobi.

+-----------------+--------+--------+---------------------------------------------------+
| Attribute       | CPLEX  | Gurobi | Description                                       |
+=================+========+========+===================================================+
| ObjCon          | ✔      | ✔      | Objective constant/offset                         |
+-----------------+--------+--------+---------------------------------------------------+
| NumStart        | ✔      | ✔      | Number of MIP starts (MIP only)                   |
+-----------------+--------+--------+---------------------------------------------------+
| NumObj          | ✔      | ✔      | Number of objectives                              |
+-----------------+--------+--------+---------------------------------------------------+

The table below shows the solution attributes supported by CPLEX and Gurobi.

+-----------------+--------+--------+---------------------------------------------------+
| Attribute       | CPLEX  | Gurobi | Description                                       |
+=================+========+========+===================================================+
| ObjVal          | ✔      | ✔      | Objective value                                   |
+-----------------+--------+--------+---------------------------------------------------+
| ObjBound        | ✔      | ✔      | Best bound (MIP only)                             |
+-----------------+--------+--------+---------------------------------------------------+
| MIPGap          | ✔      | ✔      | Relative MIP gap (MIP only)                       |
+-----------------+--------+--------+---------------------------------------------------+
| Runtime         | ✔      | ✔      | Runtime in seconds                                |
+-----------------+--------+--------+---------------------------------------------------+
| Work            | ✔      | ✔      | Work or deterministic time                        |
+-----------------+--------+--------+---------------------------------------------------+
| MaxMemUsed      |        | ✔      | Maximum amount (in GB) of memory used             |
+-----------------+--------+--------+---------------------------------------------------+
| MemUsed         |        | ✔      | Current amount (in GB) of memory used             |
+-----------------+--------+--------+---------------------------------------------------+
| SolCount        |        | ✔      | Number of solutions (MIP only)                    |
+-----------------+--------+--------+---------------------------------------------------+
| IterCount       | ✔      | ✔      | Number of simplex iterations                      |
+-----------------+--------+--------+---------------------------------------------------+
| BarIterCount    | ✔      | ✔      | Number of barrier iterations                      |
+-----------------+--------+--------+---------------------------------------------------+
| NodeCount       | ✔      | ✔      | Number of branch-and-cut nodes  (MIP only)        |
+-----------------+--------+--------+---------------------------------------------------+
| OpenNodeCount   | ✔      | ✔      | Number of open branch-and-cut nodes (MIP only)    |
+-----------------+--------+--------+---------------------------------------------------+
| NodeInt         | ✔      |        | Node number of the best solution (MIP only)       |
+-----------------+--------+--------+---------------------------------------------------+

The table below shows the solution quality attributes supported by CPLEX and Gurobi.

+-----------------+--------+--------+---------------------------------------------------+
| Attribute       | CPLEX  | Gurobi | Description                                       |
+=================+========+========+===================================================+
| MaxVio          | ✔      | ✔      | Maximum unscaled violation                        |
+-----------------+--------+--------+---------------------------------------------------+
| IntVio          | ✔      | ✔      | Maximum integrality violation                     |
+-----------------+--------+--------+---------------------------------------------------+
| Kappa           | ✔      | ✔      | Estimated condition number                        |
+-----------------+--------+--------+---------------------------------------------------+
| KappaExact      | ✔      | ✔      | Exact condition number                            |
+-----------------+--------+--------+---------------------------------------------------+
| KappaMax        | ✔      |        | Highest condition number (MIP only)               |
+-----------------+--------+--------+---------------------------------------------------+
| KappaAttention  | ✔      |        | Score of numerical difficulties (MIP only)        |
+-----------------+--------+--------+---------------------------------------------------+
| KappaStable     | ✔      |        | Percentage of stable simplex bases (MIP only)     |
+-----------------+--------+--------+---------------------------------------------------+
| KappaSuspicious | ✔      |        | Percentage of suspicious simplex bases (MIP only) |
+-----------------+--------+--------+---------------------------------------------------+
| KappaUnstable   | ✔      |        | Percentage of unstable simplex bases (MIP only)   |
+-----------------+--------+--------+---------------------------------------------------+
| KappaIllposed   | ✔      |        | Percentage of ill-posed simplex bases (MIP only)  |
+-----------------+--------+--------+---------------------------------------------------+

The table below shows the attributes for multi-objective optimization supported by CPLEX and Gurobi.
These attributes can be used to retrieve model or solution information for each subproblem solved,
as specified by the *objNo* argument.

+-----------------------------------------+--------+--------+---------------------------------------------------+
| Attribute                               | CPLEX  | Gurobi | Description                                       |
+=========================================+========+========+===================================================+
| ObjNPriority                            | ✔      | ✔      | Objective priority                                |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| ObjNCon                                 |        | ✔      | Objective constant/offset                         |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| ObjVal / ObjNVal                        | ✔      | ✔      | Objective value                                   |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| ObjBound / ObjPassNObjBound             | ✔      | ✔      | Best bound (MIP only)                             |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| MIPGap / ObjPassNMIPGap                 | ✔      | ✔      | Relative MIP gap (MIP only)                       |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| Runtime / ObjPassNRuntime               | ✔      | ✔      | Runtime in seconds                                |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| Work / ObjPassNWork                     | ✔      | ✔      | Work or deterministic time                        |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| Status / ObjPassNStatus                 | ✔      | ✔      | Solution status                                   |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| NodeCount / ObjPassNNodeCount           | ✔      | ✔      | Number of branch-and-cut nodes (MIP only)         |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| OpenNodeCount / ObjPassNOpenNodeCount   | ✔      | ✔      | Number of open branch-and-cut nodes (MIP only)    |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| IterCount / ObjPassNIterCount           | ✔      | ✔      | Number of simplex iterations                      |
+-----------------------------------------+--------+--------+---------------------------------------------------+
| BarIterCount                            | ✔      |        | Number of barrier iterations                      |
+-----------------------------------------+--------+--------+---------------------------------------------------+

For Gurobi also other model and solution attributes are supported. For a complete list; see:
`Model attributes <https://docs.gurobi.com/projects/optimizer/en/current/reference/attributes/model.html>`__.
Attributes with type ``string`` are not supported by this function.

Example
-------

In the example below two multi-objectives are specified, each with its own priority. Therefore
two subproblems are solved; one for each objective. Below we retrieve the (relative) MIP gap
for both subproblems. We also retrieve the total runtime by the solver.

.. code-block:: aimms

    myGMP := GMP::Instance::Generate( MP );

    GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 2, 1.0 );
    GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 1, 1.0 );

    GMP::Instance::Solve( myGMP );
    
    gap1 := GMP::Instance::GetAttributeValue( myGMP, "MIPGap", 1 );
    gap2 := GMP::Instance::GetAttributeValue( myGMP, "MIPGap", 2 );
    
    runtime := GMP::Instance::GetAttributeValue( myGMP, "Runtime" );

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Column::SetAsMultiObjective` and :aimms:func:`GMP::SolverSession::GetAttributeValue`.
