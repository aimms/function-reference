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

    -  This function has only meaning for generated mathematical programs
       with model type MIP, MIQP or MIQCP.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetMathematicalProgrammingType` and :aimms:func:`GMP::Instance::GetObjective`.
