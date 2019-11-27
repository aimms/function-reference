.. aimms:function:: MINLPSolutionRetrieve(n)

.. _MINLPSolutionRetrieve:

MINLPSolutionRetrieve
=====================

The procedure :aimms:func:`MINLPSolutionRetrieve` retrieves the solution
previously saved by a call to ``MINLPSolutionSave`` with solution number
``n``, and stores it as the current solution inside the AIMMS Outer
Approximation solver interface.

.. code-block:: aimms

    MINLPSolutionRetrieve(
         n       ! (input) integer scalar value
         )

Arguments
---------

    *n*
        The solution number corresponding to the solution that has to be
        retrieved. The solution number was passed to ``MINLPSolutionSave``
        before to label the solution.

Return Value
------------

    :aimms:func:`MINLPSolutionRetrieve` has no return value.
