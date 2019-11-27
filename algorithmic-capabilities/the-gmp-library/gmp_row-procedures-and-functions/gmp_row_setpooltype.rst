.. aimms:procedure:: GMP::Row::SetPoolType(GMP, row, value, mode)

.. _GMP::Row::SetPoolType:

GMP::Row::SetPoolType
=====================

The procedure :aimms:func:`GMP::Row::SetPoolType` can be used to indicate that a
row in a generated mathematical program should become part of a pool of
lazy constraints or a pool of (user) cuts. The solvers CPLEX, GUROBI and
ODH-CPLEX can make use of this information.

.. code-block:: aimms

    GMP::Row::SetPoolType(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         value,          ! (input) a scalar reference
         [mode]          ! (optional) a scalar reference
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *value*
        A scalar reference to a value. The value 1 specifies that the row should
        be added to the **lazy constraint pool** and 2 specifies that the row
        should be added to the **cut pool**. The value 0 indicates that the row
        will be removed from either pools (and treated as a normal row).

    *mode*
        A scalar reference to a value representing the lazy constraint mode. The
        value should be a number between 0 and 3. The default is 0. The meaning
        of these values is explained below.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The lazy constraint pool is supported by CPLEX, GUROBI and ODH-CPLEX
       while the cut pool is supported by CPLEX and ODH-CPLEX.

    -  Use ``GMP::Row::SetPoolTypeMulti`` if the pool type of many rows
       corresponding to some constraint have to be set, because that will be
       more efficient.

    -  The *mode* is only used if the row should be added to the lazy
       constraint pool (i.e., if *value* equals 1), and if GUROBI 7.0 or
       higher is used. The *mode* should be a value between 0 and 3, and
       these values have the following meaning:

       -  0: The mode is specified by the GUROBI option
          ``Lazy constraint mode``.

       -  1: The lazy constraint can be used to cut off a feasible solution,
          but it won't necessarily be pulled in if another lazy constraint
          also cuts off the solution.

       -  2: Lazy constraints that are violated by a feasible solution will
          be pulled into the model.

       -  3: Lazy constraints that cut off the relaxation solution at the
          root node are also pulled into the model.

.. seealso::

    The procedure :aimms:func:`GMP::Row::SetPoolTypeMulti`. The lazy constraint pool and the cut pool are
    explained in full detail in Section 14.2.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
