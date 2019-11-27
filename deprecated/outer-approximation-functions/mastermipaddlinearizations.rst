.. aimms:function:: MasterMIPAddLinearizations(IncludedConstraints, DeviationsPermitted, PenaltyMultiplier, n)

.. _MasterMIPAddLinearizations:

MasterMIPAddLinearizations
==========================

The procedure :aimms:func:`MasterMIPAddLinearizations` adds a linearization for a
subset of ``AllNonlinearConstraints``. The linearizations are created by
using the solution present at that time inside the AIMMS Outer
Approximation solver interface. Normally the solution that is returned
by the NLP solver is used. When permitted, variables are introduced to
allow for deviations from each linearized constraint. These deviation
variables are penalized in the objective function using the penalty
multipliers times the corresponding shadow prices (Lagrange
multipliers). The procedure returns the updated linearization counter in
the output argument n.

.. code-block:: aimms

    MasterMIPAddLinearizations(
         IncludedConstraints, ! (input) subset of the set AllNonlinearConstraints
         DeviationsPermitted, ! (input) 0-1 parameter over AllNonlinearConstraints
         PenaltyMultiplier,   ! (input) parameter over AllNonlinearConstraints
         n                    ! (output) integer scalar parameter
         )

Arguments
---------

    *IncludedConstraints*
        Set of nonlinear constraints for which linearizations have to be added.

    *DeviationsPermitted*
        Parameter that indicates whether or not variables should be introduced
        to allow for deviations from each linearized constraint. If so, the
        corresponding entry in this parameter should be 1, otherwise 0.

    *PenaltyMultiplier*
        The deviation variables (if any) are penalized in the objective function
        by using the values in this parameter times the corresponding shadow
        prices (Lagrange multipliers).

    *n*
        The updated linearization counter.

Return Value
------------

    :aimms:func:`MasterMIPAddLinearizations` has no return value.
