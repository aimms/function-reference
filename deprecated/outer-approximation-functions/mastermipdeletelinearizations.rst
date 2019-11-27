.. aimms:function:: MasterMIPDeleteLinearizations(n)

.. _MasterMIPDeleteLinearizations:

MasterMIPDeleteLinearizations
=============================

The procedure :aimms:func:`MasterMIPDeleteLinearizations` deletes a set of
linearizations that was previously added by the
``MasterMIPAddLinearizations`` procedure for a certain solution.

.. code-block:: aimms

    MasterMIPDeleteLinearizations(
         n       ! (input) integer scalar value
         )

Arguments
---------

    *n*
        The linearization counter for the set of linearizations that has to be
        deleted. It was returned by ``MasterMIPAddLinearizations`` when these
        linearizations were added.

Return Value
------------

    :aimms:func:`MasterMIPDeleteLinearizations` has no return value.
