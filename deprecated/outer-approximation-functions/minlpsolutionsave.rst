.. aimms:function:: MINLPSolutionSave(n)

.. _MINLPSolutionSave:

MINLPSolutionSave
=================

The procedure :aimms:func:`MINLPSolutionSave` saves the current solution that is
present inside the AIMMS Outer Approximation solver interface, and
stores it as solution number ``n`` for later retrieval.

.. code-block:: aimms

    MINLPSolutionSave(
         n       ! (input) integer scalar value
         )

Arguments
---------

    *n*
        The solution number used to label the saved solution.

Return Value
------------

    :aimms:func:`MINLPSolutionSave` has no return value.

.. note::

    If as solution was saved before with the same value for ``n`` then that
    solution will be replaced by this new solution.
