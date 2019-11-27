.. aimms:function:: MINLPSolutionDelete(n)

.. _MINLPSolutionDelete:

MINLPSolutionDelete
===================

The procedure :aimms:func:`MINLPSolutionDelete` deletes the solution inside the
AIMMS Outer Approximation solver interface that was previously saved by
a call to ``MINLPSolutionSave`` with solution number ``n``.

.. code-block:: aimms

    MINLPSolutionDelete(
         n       ! (input) integer scalar value
         )

Arguments
---------

    *n*
        The solution number corresponding to the solution that has to be
        deleted. The solution number was passed to ``MINLPSolutionSave`` before
        to label the solution.

Return Value
------------

    :aimms:func:`MINLPSolutionDelete` has no return value.
