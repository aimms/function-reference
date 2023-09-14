.. aimms:function:: GMP::Instance::GetBestBound(GMP)

.. _GMP::Instance::GetBestBound:

GMP::Instance::GetBestBound
===========================

The function :aimms:func:`GMP::Instance::GetBestBound` returns the best known
bound for a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetBestBound(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    In case of success, the function returns the best known bound. Otherwise
    it returns ``UNDF``.

.. note::
    
    -  This function can be used for GMPs with model type MIP, MIQP or MIQCP.

    -  This function can also be used for GMPs solved with BARON,
       regardless of the model type.

    -  This function can also be used for GMPs with model type QP that are
       solved with CPLEX, if the CPLEX option *Solution Target* is set to
       'Search for global optimum'.

    -  This function can also be used for GMPs with model type QP or QCP that are
       solved with GUROBI, if the GUROBI option *Nonconvex Strategy*
       is set to 'Translate'.

    -  For multi-objective models, the best bound refers to the (blended) objective
       with the highest priority.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetMathematicalProgrammingType` and :aimms:func:`GMP::Instance::GetObjective`.
