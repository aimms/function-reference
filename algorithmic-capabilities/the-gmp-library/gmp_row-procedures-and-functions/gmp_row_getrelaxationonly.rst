.. aimms:function:: GMP::Row::GetRelaxationOnly(GMP, row)

.. _GMP::Row::GetRelaxationOnly:

GMP::Row::GetRelaxationOnly
===========================

The function :aimms:func:`GMP::Row::GetRelaxationOnly` returns 1 for a row in a
generated mathematical program if it has been marked as being a
relaxation-only row; otherwise it returns 0.

.. code-block:: aimms

    GMP::Row::GetRelaxationOnly(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or the number of
        that row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    The function returns 1 if the row is a relaxation-only row, and 0
    otherwise.

.. note::

    A row is marked as being a relaxation-only row if the procedure
    :aimms:func:`GMP::Row::SetRelaxationOnly` has been called before or if the
    ``RelaxationOnly`` suffix has been set to 1 for the corresponding
    constraint.

.. seealso::

    The procedure :aimms:func:`GMP::Row::SetRelaxationOnly`. The ``RelaxationOnly`` suffix is explained in
    full detail in :ref:`sec:var.constr.glob-suff` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
