.. aimms:function:: GMP::Instance::GetNumberOfIndicatorRows(GMP)

.. _GMP::Instance::GetNumberOfIndicatorRows:

GMP::Instance::GetNumberOfIndicatorRows
=======================================

The function :aimms:func:`GMP::Instance::GetNumberOfIndicatorRows` returns the
number of indicator rows of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfIndicatorRows(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of indicator rows.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::GetNumberOfRows`.
