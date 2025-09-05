.. aimms:procedure:: GMP::Coefficient::SetMulti(GMP, binding, row, column, value)

.. _GMP::Coefficient::SetMulti:

GMP::Coefficient::SetMulti
==========================

The procedure :aimms:func:`GMP::Coefficient::SetMulti` sets the value of a range
of (linear) coefficients for a group of columns and rows, belonging to a
variable and constraint, in a generated mathematical program.

.. code-block:: aimms

    GMP::Coefficient::SetMulti(
         GMP,            ! (input) a generated mathematical program
         binding,        ! (input) an index binding
         row,            ! (input) a constraint expression
         column,         ! (input) a variable expression
         value           ! (input) a numerical expression
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *binding*
        An index binding that specifies and possibly limits the scope of
        indices.

    *row*
        A constraint that, combined with the *binding* domain, specifies the
        rows.

    *column*
        A variable that, combined with the *binding* domain, specifies the
        columns.

    *value*
        The new coefficient for each combination of row and column, defined over
        the *binding* domain.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This procedure cannot be used if the objective variable is passed
       as *column*.

    -  In case the generated mathematical program is nonlinear, this
       procedure will fail if one the columns is part of a nonlinear term in
       one of the rows. However, if the row is pure quadratic, then this
       procedure can be used to set the linear coefficient value for a
       quadratic column.

    -  GMP procedures operate on a generated mathematical program in which
       all variables are moved to the left-hand-side of each constraint.
       This can have an influence on the sign of the coeffients as
       demonstrated in the example of procedure :aimms:func:`GMP::Coefficient::Set`.

Example
-------

To set the coefficients of variable ``x(j)`` in constraint ``c(i)`` to
``coef(i,j)`` we can use: 

.. code-block:: aimms

    for (i,j) do
        GMP::Column::Set( myGMP, c(i), x(j), coef(i,j) );
    endfor;

It is more efficient to use:

.. code-block:: aimms

    GMP::Coefficient::SetMulti( myGMP, (i,j), c(i), x(j), coef(i,j) );

If we only want to set the coefficients of those ``x(j)``
for which ``dom(j)`` is unequal to zero, then we use: 

.. code-block:: aimms

    GMP::Coefficient::SetMulti( myGMP, (i,j) | dom(j), c(i), x(j), coef(i,j) );

.. seealso::

    - The routines :aimms:func:`GMP::Coefficient::Get`, :aimms:func:`GMP::Coefficient::Set` and :aimms:func:`GMP::QuadraticCoefficient::Set`.
