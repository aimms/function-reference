.. aimms:procedure:: GMP::Row::SetRelaxationOnly(GMP, row, value)

.. _GMP::Row::SetRelaxationOnly:

GMP::Row::SetRelaxationOnly
===========================

The procedure :aimms:func:`GMP::Row::SetRelaxationOnly` can be used to indicate
that a row in a generated mathematical is a relaxation-only row. Some
solvers (like BARON) can make use of this information.

.. code-block:: aimms

    GMP::Row::SetRelaxationOnly(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         value           ! (input) a scalar reference
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

    *value*
        A scalar reference to a 0-1 value.

Return Value
------------

    The procedure returns 1 on success, and 0 otherwise.

.. note::

    A row is marked as being a relaxation-only row after this procedure is
    called with the *value* argument equal to 1 or if the ``RelaxationOnly``
    suffix has been set to 1 for the corresponding constraint.

.. seealso::

    - The function :aimms:func:`GMP::Row::GetRelaxationOnly`. 
    - The ``RelaxationOnly`` suffix is explained in full detail in :ref:`sec:var.constr.glob-suff` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
