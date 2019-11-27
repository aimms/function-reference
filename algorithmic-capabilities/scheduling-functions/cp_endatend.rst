.. aimms:function:: cp::EndAtEnd(firstActivity, secondActivity, delay)

.. _cp::EndAtEnd:

cp::EndAtEnd
============

The function ``cp::EndAtEnd(a,b,d)`` returns 1 if one of the activities
:math:`a` and :math:`b` is absent, or if the end of activity :math:`a`
plus a nonnegative time period :math:`d` is equal to the end of activity
:math:`b`. The function ``cp::EndAtEnd(a,b,d)`` is equivalent to

.. math:: \begin{array}{ll} a\texttt{.Present=0} & \vee \\ b\texttt{.Present=0} & \vee \\ a\texttt{.End} + d = b\texttt{.End} & \end{array}

\ This function is typically used in scheduling constraints to place a
sequencing restriction on activities.

.. code-block:: aimms

    cp::EndAtEnd(
            firstActivity,   ! (input) an expression
            secondActivity,  ! (input) an expression
            delay            ! (optional) an expression
    )

Arguments
---------

    *firstActivity*
        An expression that results in an activity.

    *secondActivity*
        An expression that results in an activity.

    *delay*
        An optional expression that results in an integer number of time slots.
        This expression may involve variables. The default value of this
        expression is 0.

Return Value
------------

    This function returns 1 if the above condition is satisfied, and 0 if it
    is not.

.. seealso::

    -  The functions :aimms:func:`cp::BeginBeforeBegin` and :aimms:func:`cp::BeginBeforeEnd`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
