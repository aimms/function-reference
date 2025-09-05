.. aimms:procedure:: GMP::Linearization::Delete(GMP, linNo)

.. _GMP::Linearization::Delete:

GMP::Linearization::Delete
==========================

The procedure :aimms:func:`GMP::Linearization::Delete` deletes a set of rows and
columns corresponding to a linearization in a generated mathematical
program.

.. code-block:: aimms

    GMP::Linearization::Delete(
         GMP,         ! (input) a generated mathematical program
         linNo        ! (input) a linearization number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *linNo*
        An integer scalar reference to the rows and columns of the
        linearization.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    - The routines :aimms:func:`GMP::Linearization::Add` and :aimms:func:`GMP::Linearization::AddSingle`.
