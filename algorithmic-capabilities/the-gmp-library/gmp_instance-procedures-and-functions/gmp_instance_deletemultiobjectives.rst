.. aimms:procedure:: GMP::Instance::DeleteMultiObjectives(GMP)

.. _GMP::Instance::DeleteMultiObjectives:

GMP::Instance::DeleteMultiObjectives
====================================

The procedure :aimms:func:`GMP::Instance::DeleteMultiObjectives` deletes all
multi-objectives in a generated mathematical program.

.. code-block:: aimms

    GMP::Instance::DeleteMultiObjectives(
         GMP             ! (input) a generated mathematical program
         )

Arguments
---------

    *GMP*
        An element in the set :aimms:set:`AllGeneratedMathematicalPrograms`.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    A column can be specified as a multi-objective by using the procedure
    :aimms:func:`GMP::Column::SetAsMultiObjective`.

Example
-------

    In the example below two multi-objectives are specified after which a
    multi-objective optimization problem is solved. Next all
    multi-objectives are deleted by calling :aimms:func:`GMP::Instance::CreateDual`
    and the model is solved once again, this time as an ordinary
    optimization problem with one objective (namely the one specified in the
    objective attribute of the mathematical programming). 

    .. code-block:: aimms

               myGMP := GMP::Instance::Generate( MP );

               GMP::Column::SetAsMultiObjective( myGMP, TotalDist, 2, 1.0, 0, 0.1 );
               GMP::Column::SetAsMultiObjective( myGMP, TotalTime, 1, 1.0, 0, 0.0 );

               GMP::Instance::Solve( myGMP );

               GMP::Instance::DeleteMultiObjectives( myGMP );

               GMP::Instance::Solve( myGMP );

.. seealso::

    The procedure :aimms:func:`GMP::Column::SetAsMultiObjective`.
