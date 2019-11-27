.. aimms:function:: MasterMIPLinearizationCommand(n, ModelConstraint, Command, CommandData)

.. _MasterMIPLinearizationCommand:

MasterMIPLinearizationCommand
=============================

The procedure :aimms:func:`MasterMIPLinearizationCommand` allows you to retrieve
or modify certain aspects of the linearization of a constraint added for
linearization counter ``n`` at the individual level. The argument
``Command`` specifies which data (e.g. GetDeviation) should be retrieved
or modified. The retrieved or modified value is passed through the
``CommandData`` argument.

.. code-block:: aimms

    MasterMIPLinearizationCommand(
         n,                ! (input) integer scalar value
         ModelConstraint,  ! (input) scalar value
         Command,          ! (input) element parameter into
                           !         MasterMIPLinearizationCommands
         CommandData       ! (inout) scalar value (in) or parameter (out)
         )

Arguments
---------

    *n*
        The linearization counter as returned by ``MasterMIPAddLinearizations``
        when adding this linearization.

    *ModelConstraint*
        Scalar reference to a constraint for which certain aspects of the
        linearization have to be retrieved or modified.

    *Command*
        Element parameter into ``MasterMIPLinearizationCommands`` that specifies
        which data should be retrieved or modified. Possible values are:

        ========================= ======================================================================================
        **Command**               **Description**
        ========================= ======================================================================================
        ``GetDeviation``          Get the value of the deviation variable.
        ``RemoveDeviation``       Delete the deviation variable.
        ``GetWeight``             Get the objective coefficient of the deviation variable.
        ``SetWeight``             Set the objective coefficient of the deviation variable.
        ``GetDeviationBound``     Get the upper bound of the deviation variable.
        ``SetDeviationBound``     Get the upper bound of the deviation variable.
        ``GetLagrangeMultiplier`` Get value of the shadow price (Lagrange multiplier) of constraint for last solved NLP.
        ========================= ======================================================================================

    *CommandData*
        The retrieved or modified value.

Return Value
------------

    :aimms:func:`MasterMIPLinearizationCommand` has no return value.

.. note::

    -  Normally, the weight obtained with 'GetWeight' equals the value of
       the penalty multiplier, as passed to ``MasterMIPAddLinearizations``,
       times the shadow price (Lagrange multiplier) of the constraint. With
       'SetWeight' this weight can be changed.

    -  Note that 'SetWeight' can be used to create a deviation variable
       (slack) if the linearization does not have one. To do so the value
       filled in for ``CommandData`` should be unequal to 0.

    -  The lower bound of a deviation variable always equals 0.
