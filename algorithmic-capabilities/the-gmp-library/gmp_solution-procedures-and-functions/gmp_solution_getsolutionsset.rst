.. aimms:function:: GMP::Solution::GetSolutionsSet(GMP)

.. _GMP::Solution::GetSolutionsSet:

GMP::Solution::GetSolutionsSet
==============================

The function :aimms:func:`GMP::Solution::GetSolutionsSet` returns the set of
non-empty solutions in the solution repository of a generated
mathematical program.

.. code-block:: aimms

    GMP::Solution::GetSolutionsSet(
         GMP            ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    A subset of :aimms:set:`Integers`.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Solution::Count` and the section on Managing the
    solution repository Section 16.4 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
