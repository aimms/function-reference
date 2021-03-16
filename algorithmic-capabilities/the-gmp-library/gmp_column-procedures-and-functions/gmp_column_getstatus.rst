.. aimms:function:: GMP::Column::GetStatus(GMP, column)

.. _GMP::Column::GetStatus:

GMP::Column::GetStatus
======================

The function :aimms:func:`GMP::Column::GetStatus` returns the status of a column
in the matrix of a generated mathematical program.

.. code-block:: aimms

    GMP::Column::GetStatus(
         GMP,            ! (input) a generated mathematical program
         column          ! (input) a scalar reference or column number
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *column*
        A scalar reference to an existing column in the matrix or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

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

    -  This function will return '\ ``PresolveDeleted``\ ' only if the
       generated mathematical program has been created with
       ``GMP::Instance::CreatePresolved``. Status '\ ``PresolveDeleted``\ '
       means that the column was generated for the original generated
       mathematical program but deleted when the presolved mathematical
       program was created.

    -  Status '\ ``Deactivated``\ ' is not possible for columns.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate` and :aimms:func:`GMP::Instance::CreatePresolved`.
