.. aimms:function:: GMP::Solution::GetBestBound(GMP, solution)

.. _GMP::Solution::GetBestBound:

GMP::Solution::GetBestBound
===========================

The function :aimms:func:`GMP::Solution::GetBestBound` returns the the best known
bound on a solution.

.. code-block:: aimms

    GMP::Solution::GetBestBound(
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

    In case of success, the best known bound. Otherwise it returns ``UNDF``.

.. note::

    -  This function has only meaning for a generated mathematical program
       with model type MIP, MIQP or MIQCP.

    -  

.. seealso::

    The procedure :aimms:func:`GMP::Solution::GetObjective`.
