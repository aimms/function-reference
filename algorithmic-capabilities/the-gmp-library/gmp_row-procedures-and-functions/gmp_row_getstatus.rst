.. aimms:function:: GMP::Row::GetStatus(GMP, row)

.. _GMP::Row::GetStatus:

GMP::Row::GetStatus
===================

The function :aimms:func:`GMP::Row::GetStatus` returns the status of a row in the
matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Row::GetStatus(
         GMP,            ! (input) a generated mathematical program
         row             ! (input) a scalar reference or row number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the matrix or an element in the
        set :aimms:set:`Integers` in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the
        number of rows in the matrix.

Return Value
------------

    An element in the predefined set :aimms:set:`AllRowColumnStatuses`. The set
    :aimms:set:`AllRowColumnStatuses` contains the following elements:

    -  Active,

    -  Deactivated,

    -  Deleted,

    -  NotGenerated,

    -  PresolveDeleted.

.. note::

    This function will return '\ ``PresolveDeleted``\ ' only if the
    generated mathematical program has been created with
    :aimms:func:`GMP::Instance::CreatePresolved`. Status '\ ``PresolveDeleted``\ '
    means that the row was generated for the original generated mathematical
    program but deleted when the presolved mathematical program was created.

.. seealso::

    - The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::CreatePresolved`.
