.. aimms:procedure:: GMP::Solution::Delete(GMP, solution)

.. _GMP::Solution::Delete:

GMP::Solution::Delete
=====================

The procedure :aimms:func:`GMP::Solution::Delete` deletes a solution from the
solution repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::Delete(
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

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::DeleteAll`.
