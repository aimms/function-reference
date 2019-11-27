.. aimms:function:: cp::ActivitySize(optionalActivity, absentValue)

.. _cp::ActivitySize:

cp::ActivitySize
================

The function ``cp::ActivitySize(a,d)`` returns the size of activity
:math:`a` when it is present or default value :math:`d` when it is
absent.

Mathematical Formulation
------------------------

    The function ``cp::ActivitySize(a,d)`` is equivalent to

    .. math:: \left\{ \begin{array}{ll} a.\texttt{size} & \textrm{if } a.\texttt{present} \\ d & \textrm{otherwise } \end{array} \right.

    \ This function is typically used in scheduling problems to link
    activities to other components of the problem.

    .. code-block:: aimms

        cp::ActivitySize(
                optionalActivity,   ! (input) an expression
                absentValue         ! (input) an expression
        )

Arguments
---------

    *optionalActivity*
        An expression resulting in an activity. This activity may have the
        property ``optional``.

    *absentValue*
        An expression that results in the value used when activity
        ``optionalActivity`` is absent. This expression cannot involve
        variables.

Return Value
------------

    This function returns the size of an activity when that activity is
    present or a specified default value when it is not.

Example
-------

    In the example below, we require that the size of the shift represented
    by element variable ``evShift`` matches the size of the optional
    activity ``myAct``. 

    .. code-block:: aimms

                Constraint linkShiftActivity {
                    Definition :  cp::ActivitySize( myAct, 3) =, shiftSize(evShift);
                }

.. seealso::

    The functions :aimms:func:`cp::Count` and :aimms:func:`cp::ActivityBegin`.
