.. aimms:function:: NLPLinearizationPointHasBeenFound(None)

.. _NLPLinearizationPointHasBeenFound:

NLPLinearizationPointHasBeenFound
=================================

The function :aimms:func:`NLPLinearizationPointHasBeenFound` indicates whether the
NLP solver has found a point that can be used to linearize the nonlinear
constraints. If the NLP problem is infeasible then usually the NLP
solver provides a point that solves the so-called feasibility problem
(i.e., a point that minimizes the sum of the infeasibilities).

.. code-block:: aimms

    NLPLinearizationPointHasBeenFound

Arguments
---------

    *None*

Return Value
------------

    The function :aimms:func:`NLPLinearizationPointHasBeenFound` returns 1 if the NLP
    solver has found a point that can be used to linearize the nonlinear
    constraints. It returns 0 otherwise.

.. note::

    This function always returns 1 if the NLP has found a feasible solution.
