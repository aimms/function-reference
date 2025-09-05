.. aimms:procedure:: GMP::Robust::EvaluateAdjustableVariables(GMP, Variables, merge)

.. _GMP::Robust::EvaluateAdjustableVariables:

GMP::Robust::EvaluateAdjustableVariables
========================================

The procedure :aimms:func:`GMP::Robust::EvaluateAdjustableVariables` evaluates the
values of a set of adjustable variables using the current values of the
uncertain parameters inside the model.

.. code-block:: aimms

    GMP::Robust::EvaluateAdjustableVariables(
         GMP,              ! (input) a generated mathematical program
         Variables,        ! (input) a set of variables
         [merge]           ! (optional, default 0) a scalar value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *Variables*
        A subset of :aimms:set:`AllVariables`.

    *merge*
        A scalar binary value to indicate whether the evaluated values for the
        adjustable variables should be merged with the existing values (value 1)
        or should replace them (value 0).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  The *GMP* must have been created using the procedure
       :aimms:func:`GMP::Instance::GenerateRobustCounterpart`.

    -  This procedure will ignore variables in the set *Variables* that are
       not part of the *GMP*. It will also ignore non-adjustable variables.

    -  The evaluated values will be stored in the ``.robust`` suffix of the
       adjustable variables. (Note that no values are stored inside this
       suffix after the robust counterpart is solved.)

    -  This procedure will fail if the option ``Keep`` ``Uncertain``
       ``Mathematical`` ``Program`` was not switched on before calling
       procedure :aimms:func:`GMP::Instance::GenerateRobustCounterpart`.

Example
-------

Assume that ``rcGMP`` is a robust counterpart GMP with one adjustable
variable ``Production(i,t)`` that depends on the uncertain parameter
``Demand(s)``. After solving the robust counterpart you can calculate
the values of ``Production`` for a certain realization of ``Demand`` as
follows: 

.. code-block:: aimms

    Demand(s) := 5;

    GMP::Robust::EvaluateAdjustableVariables( rcGMP, AllVariables );

It is also possible to calculate the values of the
adjustable variables without using this procedure: 

.. code-block:: aimms

    Demand(s) := 5;

    CalculatedProduction(i,t) := Production.adjustable.Constant(i,t) +
        sum( s, Demand(s) * Production.adjustable.Demand(i,t,s) );

Here
``CalculatedProduction(i,t)`` is a parameter used to store the
calculated values of ``Production(i,t)``.

.. seealso::

    - The function :aimms:func:`GMP::Instance::GenerateRobustCounterpart`.
