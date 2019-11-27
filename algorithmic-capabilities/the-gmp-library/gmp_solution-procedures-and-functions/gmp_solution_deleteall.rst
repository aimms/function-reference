.. aimms:procedure:: GMP::Solution::DeleteAll(GMP)

.. _GMP::Solution::DeleteAll:

GMP::Solution::DeleteAll
========================

The procedure :aimms:func:`GMP::Solution::DeleteAll` empties the solution
repository of a generated mathematical program.

.. code-block:: aimms

    GMP::Solution::DeleteAll(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::Delete`.
