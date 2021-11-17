.. aimms:procedure:: GMP::Column::AddMulti(GMP, binding, column)

.. _GMP::Column::AddMulti:

GMP::Column::AddMulti
=====================

The procedure :aimms:func:`GMP::Column::AddMulti` adds a group of columns, belonging
to a variable, to a generated mathematical program.

.. code-block:: aimms

    GMP::Column::AddMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         column          ! (input) a variable expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *column*
        A variable that, combined with the *binding* domain, specifies the
        columns.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    Coefficients for these columns can be added to the matrix by using the
    procedure :aimms:func:`GMP::Coefficient::Set`. After calling :aimms:func:`GMP::Column::AddMulti`
    the type and the lower and upper bound of the columns are set according
    to the definition of the corresponding symbolic variable. By using the
    procedures :aimms:func:`GMP::Column::SetType`, :aimms:func:`GMP::Column::SetLowerBound` and
    :aimms:func:`GMP::Column::SetUpperBound` the column types and the lower and upper
    bounds can be changed.

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Coefficient::Set`, :aimms:func:`GMP::Column::Add`, :aimms:func:`GMP::Column::Delete`, :aimms:func:`GMP::Column::SetType`, :aimms:func:`GMP::Column::SetLowerBound` and
    :aimms:func:`GMP::Column::SetUpperBound`.
