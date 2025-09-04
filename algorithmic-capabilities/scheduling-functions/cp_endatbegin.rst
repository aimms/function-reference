.. aimms:function:: cp::EndAtBegin(firstActivity, secondActivity, delay)

.. _cp::EndAtBegin:

cp::EndAtBegin
==============

The function ``cp::EndAtBegin(a,b,d)`` returns 1 if one of the
activities :math:`a` and :math:`b` is absent, or if the begin of
activity :math:`a` plus a nonnegative time period :math:`d` is equal to
the begin of activity :math:`b`. The function ``cp::EndAtBegin(a,b,d)``
is equivalent to

.. math:: \begin{array}{ll} a\texttt{.Present=0} & \vee \\ b\texttt{.Present=0} & \vee \\ a\texttt{.End} + d = b\texttt{.Begin} & \end{array}

\ This function is typically used in scheduling constraints to place a
sequencing restriction on activities.

.. code-block:: aimms

    cp::EndAtBegin(
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

    -  The functions :aimms:func:`cp::BeginBeforeBegin` and :aimms:func:`cp::BeginBeforeEnd`.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
