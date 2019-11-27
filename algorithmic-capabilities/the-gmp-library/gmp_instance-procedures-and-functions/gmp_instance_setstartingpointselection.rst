.. aimms:procedure:: GMP::Instance::SetStartingPointSelection(GMP, selectedColumnNumbers)

.. _GMP::Instance::SetStartingPointSelection:

GMP::Instance::SetStartingPointSelection
========================================

The procedure :aimms:func:`GMP::Instance::SetStartingPointSelection` specifies a
selection of columns for which an initial value is given. This selection
is only used for mathematical programs of type ``COP`` and ``CSP``.

.. code-block:: aimms

    GMP::Instance::SetStartingPointSelection(
         GMP,                  ! (input) a generated mathematical program
         selectedColumnNumbers ! (input) a subset of Integers
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *selectedColumnNumbers*
        An expression that results in a subset of the set :aimms:set:`Integers`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::GetColumnNumbers` and :aimms:func:`GMP::Instance::Solve`.
