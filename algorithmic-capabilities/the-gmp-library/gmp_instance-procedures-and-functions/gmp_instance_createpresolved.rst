.. aimms:function:: GMP::Instance::CreatePresolved(GMP, name)

.. _GMP::Instance::CreatePresolved:

GMP::Instance::CreatePresolved
==============================

The function :aimms:func:`GMP::Instance::CreatePresolved` generates a mathematical
program that is the presolved representation of the specified generated
mathematical program. The generated mathematical program can be a linear
or nonlinear model, and should be generated using the function
``GMP::Instance::Generate``.

.. code-block:: aimms

    GMP::Instance::CreatePresolved(
         GMP,            ! (input) a generated mathematical program
         name            ! (input) a string expression
    )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

    *name*
        A string that holds the name for the presolved mathematical program.

Return Value
------------

    A new element in the set :aimms:set:`AllGeneratedMathematicalPrograms`, with the name as specified by the
    *name* argument, if the presolver did not find an infeasibility. Else,
    the empty element.

.. note::

    -  By using the functions ``GMP::Column::GetStatus`` and
       ``GMP::Row::GetStatus`` it is possible to check whether a column or
       row was deleted when the presolved mathematical program was created.

    -  By using the functions ``GMP::Column::GetLowerBound`` and
       ``GMP::Column::GetUpperBound`` it is possible to retrieve the lower
       and upper bound of a column in the presolved mathematical program.

    -  If the original *GMP* is deleted then the presolved GMP created by
       :aimms:func:`GMP::Instance::CreatePresolved` will also be deleted.

    -  If the option ``MINLP Probing`` is switched on, then this function
       will change the mathematical programming type from MINLP (NLP) into
       MIP (LP) if the presolved model contains no nonlinear constraints.

Example
-------

    Assume that 'MP' is a mathematical program and 'gmpMP' and 'gmpPre' are
    element parameters with range :aimms:set:`AllGeneratedMathematicalPrograms`. To solve the presolved model
    using GMP functions we can use: 

    .. code-block:: aimms

               gmpMP := GMP::Instance::Generate( MP );
               gmpPre := GMP::Instance::CreatePresolved( gmpMP, "PresolvedModel" );

               GMP::Instance::Solve( gmpPre ) ;

    In case the GMP variant of
    the AOA module is used we can use: 

    .. code-block:: aimms

               gmpMP := GMP::Instance::Generate( MP );
               gmpPre := GMP::Instance::CreatePresolved( gmpMP, "PresolvedModel" );

               GMPOuterApprox::DoOuterApproximation( gmpPre );

    Here 'GMPOuterApprox' is
    the prefix used by the GMP Outer Approximation Module.

.. seealso::

    The functions :aimms:func:`GMP::Instance::Delete`, :aimms:func:`GMP::Instance::Generate`, :aimms:func:`GMP::Instance::Solve`, :aimms:func:`GMP::Column::GetStatus`, :aimms:func:`GMP::Row::GetStatus`,
    :aimms:func:`GMP::Column::GetLowerBound` and :aimms:func:`GMP::Column::GetUpperBound`.
