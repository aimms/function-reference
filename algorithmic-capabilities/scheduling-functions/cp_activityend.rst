.. aimms:function:: cp::ActivityEnd(optionalActivity, absentValue)

.. _cp::ActivityEnd:

cp::ActivityEnd
===============

The function ``cp::ActivityEnd(a,d)`` returns the end of activity
:math:`a` if it is present or default value :math:`d` when it is absent.

Mathematical Formulation
------------------------

The function ``cp::ActivityEnd(a,d)`` is equivalent to

.. math:: \left\{ \begin{array}{ll} a.\texttt{end} & \textrm{if } a.\texttt{present} \\ d & \textrm{otherwise } \end{array} \right.

\ This function is typically used in scheduling problems to link
activities to other components of the problem.

.. code-block:: aimms

    cp::ActivityEnd(
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
        ``optionalActivity`` is absent. The result of this expression is an
        element in the schedule domain of the activity. This expression cannot
        involve variables.

Return Value
------------

    This function returns an element in the schedule domain of the activity
    and this element is the end of an activity when that activity is present
    or a specified default value when it is not.

Example
-------

In the example below, we require that the end of the shift represented
by element variable ``evShift`` matches the end of the optional activity
``myAct``. 

.. code-block:: aimms

    Constraint linkShiftActivity {
        Definition :  cp::ActivityEnd( myAct, last(myCal)) = endHour(evShift);
    }

.. seealso::

    - The functions :aimms:func:`cp::Count` and :aimms:func:`cp::ActivityBegin`.
