.. aimms:function:: cp::ActivityLength(optionalActivity, absentValue)

.. _cp::ActivityLength:

cp::ActivityLength
==================

The function ``cp::ActivityLength(a,d)`` returns the length of activity
:math:`a` when present and default value :math:`d` when absent.

Mathematical Formulation
------------------------

The function ``cp::ActivityLength(a,d)`` is equivalent to

.. math:: \left\{ \begin{array}{ll} a.\texttt{length} & \textrm{if } a.\texttt{present} \\ d & \textrm{otherwise } \end{array} \right.

\ This function is typically used in scheduling problems to link
activities to other components of the problem.

.. code-block:: aimms

    cp::ActivityLength(
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

    This function returns the length of an activity when that activity is
    present or a specified default value when it is not.

Example
-------

In the example below, we require that the length of an activity is 36,
whether or not it is present. When the length of an activity is fixed,
if it is present, then this type of constraint might improve the
performance of the CP solver. 

.. code-block:: aimms

    Constraint linkShiftActivity {
        Definition :  cp::ActivityLength( myAct, 36 ) = 36;
    }

Note that the above constraint
is automatically generated when the length attribute of activity
``myAct`` is specified as ``36``.

.. seealso::

    - The functions :aimms:func:`cp::Count` and :aimms:func:`cp::ActivityBegin`.
