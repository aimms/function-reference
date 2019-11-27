.. aimms:function:: cp::EndBeforeEnd(firstActivity, secondActivity, delay)

.. _cp::EndBeforeEnd:

cp::EndBeforeEnd
================

The function ``cp::EndBeforeEnd(a,b,d)`` returns 1 if one of the
activities :math:`a` and :math:`b` is absent, or if the end of activity
:math:`a` plus a nonnegative time period :math:`d` is less than or equal
to the end of activity :math:`b`. The function
``cp::EndBeforeEnd(a,b,d)`` is equivalent to

.. math:: \begin{array}{ll} a\texttt{.Present=0} & \vee \\ b\texttt{.Present=0} & \vee \\ a\texttt{.End} + d \leq b\texttt{.End} & \end{array}

\ This function is typically used in scheduling constraints to place a
sequencing restriction on activities.

.. code-block:: aimms

    cp::EndBeforeEnd(
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

    -  The functions :aimms:func:`cp::EndAtEnd` and :aimms:func:`cp::EndBeforeBegin`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
