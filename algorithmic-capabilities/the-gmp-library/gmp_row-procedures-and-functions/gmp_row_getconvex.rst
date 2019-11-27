.. aimms:function:: GMP::Row::GetConvex(GMP, row)

.. _GMP::Row::GetConvex:

GMP::Row::GetConvex
===================

The function :aimms:func:`GMP::Row::GetConvex` returns 1 for a row in a generated
mathematical program if it has been marked as being convex; otherwise it
returns 0.

.. code-block:: aimms

    GMP::Row::GetConvex(
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

    The function returns 1 if the row is convex, and 0 otherwise.

.. note::

    AIMMS cannot detect whether a row is convex or not. A row is marked as
    being convex if the procedure ``GMP::Row::SetConvex`` has been called
    before or if the ``Convex`` suffix has been set to 1 for the
    corresponding constraint.

.. seealso::

    The procedure :aimms:func:`GMP::Row::SetConvex`. The ``Convex`` suffix is explained in full
    detail in Section 14.2.6 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
