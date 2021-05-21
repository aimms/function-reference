.. aimms:procedure:: GMP::Row::SetPoolTypeMulti(GMP, binding, row, value, mode)

.. _GMP::Row::SetPoolTypeMulti:

GMP::Row::SetPoolTypeMulti
==========================

The procedure :aimms:func:`GMP::Row::SetPoolTypeMulti` can be used to indicate
that a group of rows, belonging to a constraint in a generated
mathematical program, should become part of a pool of lazy constraints or
a pool of (user) cuts. The solvers CPLEX, Gurobi and ODH-CPLEX can make
use of this information.

.. code-block:: aimms

    GMP::Row::SetPoolTypeMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row,            ! (input) a constraint expression
         value,          ! (input) a numerical expression
         mode            ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *row*
        A constraint that, combined with the ``binding`` domain, specifies the
        rows.

    *value*
        The pool type for each row, defined over the binding domain ``binding``.
        A value of 1 specifies that the row should be added to the **lazy
        constraint pool** and 2 specifies that the row should be added to the
        **cut pool**. The value 0 indicates that the row will be removed from
        either pools (and treated as a normal row).

    *mode*
        The lazy constraint mode for each row, defined over the binding domain
        ``binding``. Its value should be a number between 0 and 3. The meaning
        of these values is explained below.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    -  The lazy constraint pool is supported by CPLEX, Gurobi and ODH-CPLEX
       while the cut pool is supported by CPLEX and ODH-CPLEX.

    -  The *mode* is only used if the row should be added to the lazy
       constraint pool (i.e., if *value* equals 1) and if Gurobi is used.
       The *mode* should be a value between 0 and 3, and
       these values have the following meaning:

       -  0: The mode is specified by the Gurobi option
          ``Lazy constraint mode``.

       -  1: The lazy constraint can be used to cut off a feasible solution,
          but it won't necessarily be pulled in if another lazy constraint
          also cuts off the solution.

       -  2: Lazy constraints that are violated by a feasible solution will
          be pulled into the model.

       -  3: Lazy constraints that cut off the relaxation solution at the
          root node are also pulled into the model.

.. seealso::

    The procedure :aimms:func:`GMP::Row::SetPoolType`. The lazy constraint pool and the cut pool are
    explained in full detail in :ref:`sec:var.constr.indicator` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
