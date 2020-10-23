.. aimms:procedure:: GMP::Row::GenerateMulti(GMP, row, autoAddColumn)

.. _GMP::Row::GenerateMulti:

GMP::Row::GenerateMulti
=======================

The procedure :aimms:func:`GMP::Row::GenerateMulti` generates a group of rows, belonging to a constraint,
and adds them to the matrix of a generated mathematical program. The rows are generated according
to the definition of the associated symbolic constraint, or to the definition of the associated
symbolic variable in case the rows refer to the definition of a variable.

.. code-block:: aimms

    GMP::Row::GenerateMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row,            ! (input) a constraint expression
         [autoAddColumn] ! (optional) a binary scalar
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *row*
        A constraint that, combined with the ``binding`` domain, specifies the
        rows.

    *autoAddColumn*
        A binary scalar indicating whether this procedure should automatically
        add columns that are not in the *GMP*. The default is 0 meaning that no
        columns are added.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Before generating the rows all existing matrix coefficients for
       this group of rows are removed.

    -  The row types and the right-hand-side values (and, if the row type is
       ``'ranged'``, the left-hand-side values) are set according to the
       constraint definition.

    -  This procedure cannot be used if one of the rows contains the objective variable,
       and the row was added or generated before using a different coefficient for the
       objective variable.

    -  If the value of *autoAddColumn* equals 0, then this procedure will
       generate an error if it encounters a column that is not in the *GMP*.
       You then have to add that column before calling this procedure by
       using the procedure ``GMP::Column::Add``.

    -  Setting the value of *autoAddColumn* to 1 should only be done if
       you know exactly which columns are automatically added by this procedure.
       Otherwise you might end up with a model in which some columns only appear in
       one of these rows, possibly making this row redundant.

    -  This procedure will never add columns that were deleted before with
       the procedure ``GMP::Column::Delete``.

Example
-------

    To generate the rows corresponding to constraint ``c(i)`` we can use: 

    .. code-block:: aimms

               GMP::Row::GenerateMulti( myGMP, i, c(i) );

    If the row refers to the definition of
    a variable then we have to place '\_definition' behind the name of the
    variable. For example, if ``v(j)`` is a variable with a definition and
    we want to generate all corresponding rows according to its definition
    then we have to use:

    .. code-block:: aimms

               GMP::Row::GenerateMulti( myGMP, j, v_definition(j) );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::Add`, :aimms:func:`GMP::Column::Delete`, :aimms:func:`GMP::Row::Add`, :aimms:func:`GMP::Row::Delete` and :aimms:func:`GMP::Row::Generate`.
