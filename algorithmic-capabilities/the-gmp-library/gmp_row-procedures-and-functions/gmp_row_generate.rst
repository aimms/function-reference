.. aimms:procedure:: GMP::Row::Generate(GMP, row, autoAddColumn)

.. _GMP::Row::Generate:

GMP::Row::Generate
==================

The procedure :aimms:func:`GMP::Row::Generate` generates a row and adds it to the
matrix of a generated mathematical program. The row is generated
according to the definition of its associated symbolic constraint, or to
the definition of its associated symbolic variable in case the row
refers to the definition of a variable.

.. code-block:: aimms

    GMP::Row::Generate(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference
         [autoAddColumn] ! (optional) a binary scalar
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to a row.

    *autoAddColumn*
        A binary scalar indicating whether this procedure should automatically
        add columns that are not in the *GMP*. The default is 0 meaning that no
        columns are added.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Before generating the row all existing matrix coefficients for this
       row are removed.

    -  The row type and the right-hand-side value (and, if the row type is
       ``'ranged'``, the left-hand-side value) are set according to the
       constraint definition.

    -  This procedure cannot be used if the row contains the objective
       variable, and the row was added or generated before using a different
       coefficient for the objective variable.

    -  If the value of *autoAddColumn* equals 0, then this procedure will
       generate an error if it encounters a column that is not in the *GMP*.
       You then have to add that column before calling this procedure by
       using the procedure ``GMP::Column::Add``.

    -  Setting the value of *autoAddColumn* to 1 should only be done if you
       know exactly which columns are automatically added by this procedure.
       Otherwise you might end up with a model in which some columns only
       appear in this row, possibly making this row redundant.

    -  This procedure will never add columns that were deleted before with
       the procedure ``GMP::Column::Delete``.

Example
-------

    To generate the row corresponding to constraint ``c(i)`` for element
    ``'1'``, we can use: 

    .. code-block:: aimms

               GMP::Row::Generate( myGMP, c('1') );

    If the row refers to the definition of
    a variable then we have to place '\_definition' behind the name of the
    variable. For example, if ``v(j)`` is a variable with a definition and
    we want to generate a row according to its definition for element
    ``'2'`` then we have to use: 

    .. code-block:: aimms

               GMP::Row::Generate( myGMP, v_definition('2') );

.. seealso::

    The routines :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Column::Add`, :aimms:func:`GMP::Column::Delete`, :aimms:func:`GMP::Row::Add` and :aimms:func:`GMP::Row::Delete`.
