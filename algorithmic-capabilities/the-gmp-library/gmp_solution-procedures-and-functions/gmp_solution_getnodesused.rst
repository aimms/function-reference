.. aimms:function:: GMP::Solution::GetNodesUsed(GMP, solution)

.. _GMP::Solution::GetNodesUsed:

GMP::Solution::GetNodesUsed
===========================

The function :aimms:func:`GMP::Solution::GetNodesUsed` returns the number of nodes
used to create a solution in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::GetNodesUsed(
         GMP,            ! (input) a generated mathematical program
         solution        ! (input) a solution
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *solution*
        An integer scalar reference to a solution.

Return Value
------------

    The number of nodes used to create a solution.

.. note::

    -  This function has only meaning for solver sessions belonging to a GMP
       with type MIP, MIQP or MIQCP.

    -  This function can be used inside a **candidate**, **cut** or
       **heuristic** callback.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::SetCallbackAddCut`, :aimms:func:`GMP::Instance::SetCallbackCandidate` and :aimms:func:`GMP::Instance::SetCallbackHeuristic`.
