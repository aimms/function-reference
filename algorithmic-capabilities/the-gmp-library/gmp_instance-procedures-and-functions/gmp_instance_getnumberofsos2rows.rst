.. aimms:function:: GMP::Instance::GetNumberOfSOS2Rows(GMP)

.. _GMP::Instance::GetNumberOfSOS2Rows:

GMP::Instance::GetNumberOfSOS2Rows
==================================

The function :aimms:func:`GMP::Instance::GetNumberOfSOS2Rows` returns the number
of SOS rows of type 2 of a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::GetNumberOfSOS2Rows(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The function returns the number of SOS rows of type 2.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetNumberOfRows` and :aimms:func:`GMP::Instance::GetNumberOfSOS1Rows`.
