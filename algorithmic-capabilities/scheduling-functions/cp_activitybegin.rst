.. aimms:function:: cp::ActivityBegin(optionalActivity, absentValue)

.. _cp::ActivityBegin:

cp::ActivityBegin
=================

The function ``cp::ActivityBegin(a,d)`` returns the begin of activity
:math:`a` when it is present or default value :math:`d` when it is
absent.

Mathematical Formulation
------------------------

The function ``cp::ActivityBegin(a,d)`` is equivalent to

.. math:: \left\{ \begin{array}{ll} a.\texttt{begin} & \textrm{if } a.\texttt{present} \\ d & \textrm{otherwise } \end{array} \right.

\ This function is typically used in scheduling problems to link
activities to other components of the problem.

.. code-block:: aimms

    cp::ActivityBegin(
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
    and this element is the begin of an activity when that activity is
    present or a specified default value when it is not.

Example
-------

In the example below, we require that the beginning of the shift
represented by element variable ``evShift`` matches the begin of the
optional activity ``myAct``. 

.. code-block:: aimms

    Constraint linkShiftActivity {
        Definition :  cp::ActivityBegin( myAct, first(myCal)) = beginHour(evShift) );
    }

.. seealso::

    - The functions :aimms:func:`cp::Count` and :aimms:func:`cp::ActivityEnd`.
