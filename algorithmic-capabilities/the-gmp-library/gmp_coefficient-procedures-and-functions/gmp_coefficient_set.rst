.. aimms:procedure:: GMP::Coefficient::Set(GMP, row, column, value)

.. _GMP::Coefficient::Set:

GMP::Coefficient::Set
=====================

The procedure :aimms:func:`GMP::Coefficient::Set` sets the value of a (linear)
coefficient in a generated mathematical program.

.. code-block:: aimms

    GMP::Coefficient::Set(
         GMP,            ! (input) a generated mathematical program
         row,            ! (input) a scalar reference or row number
         column,         ! (input) a scalar reference or column number
         value           ! (input) a scalar numerical value
         )

Arguments
---------

    *GMP*
        An element in :aimms:set:`AllGeneratedMathematicalPrograms`.

    *row*
        A scalar reference to an existing row in the model or the number of that
        row in the range :math:`\{ 0 .. m-1 \}` where :math:`m` is the number of
        rows in the matrix.

    *column*
        A scalar reference to an existing column in the model or the number of
        that column in the range :math:`\{ 0 .. n-1 \}` where :math:`n` is the
        number of columns in the matrix.

    *value*
        A scalar numerical value indicating the value for the coefficient.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  Use ``GMP::Coefficient::SetMulti`` if many coefficients have to be
       set because that will be more efficient.

    -  This procedure cannot be used if the column refers to the objective
       variable.

    -  In case the generated mathematical program is nonlinear, this
       procedure will fail if the column is part of a nonlinear term in the
       row. However, if the row is pure quadratic, then this procedure can
       be used to set the linear coefficient value for a quadratic column.

    -  GMP procedures operate on a generated mathematical program in which
       all variables are moved to the left-hand-side of each constraint.
       This can have an influence on the sign of the coeffients as
       demonstrated in the example below.

Example
-------

    | Assume that we have the following variable and constraint declarations
      (in aim format):. 

      .. code-block:: aimms

                 Variable y;
                 Variable z;
                 Variable x1;
                 Constraint e1 {
                     Definition :  x1 - 2*y - 3*z = 0;
                 }
                 Variable x2 {
                     Definition :  2*y + 3*z;
                 }

    | To change the coefficient of variable
      :math:`\verb|y|` in constraint :math:`\verb|e1|` to 4 we use:

      .. code-block:: aimms

                 GMP::Coefficient::Set( myGMP, e1, y, 4 );

    | This results in the row :math:`\verb|x1 + 4*y - 3*z = 0|`.

    | The definition of variable :math:`\verb|x2|` is generated as the row
      :math:`\verb|x2 - 2*y - 3*z = 0|` by AIMMS. Therefore, using

      .. code-block:: aimms

                 GMP::Coefficient::Set( myGMP, x2_definition, y, -4 );

      will result in the row :math:`\verb|x2 - 4*y - 3*z = 0|`.

.. seealso::

    The routines :aimms:func:`GMP::Coefficient::Get`, :aimms:func:`GMP::Coefficient::SetMulti` and :aimms:func:`GMP::QuadraticCoefficient::Set`.
