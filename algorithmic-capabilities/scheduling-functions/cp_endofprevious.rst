.. aimms:function:: cp::EndOfPrevious(sequentialResource, scheduledActivity, firstValue, absentValue)

.. _cp::EndOfPrevious:

cp::EndOfPrevious
=================

The function :aimms:func:`cp::EndOfPrevious` refers to the end of the previous
activity in a sequence of activities. For a resource :math:`r`, an
activity :math:`a`, timeslots :math:`f` and :math:`d`, the function
``cp::EndOfPrevious(r,a,f,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`f` if :math:`a` is present and scheduled as the first activity
   on :math:`r`, and

-  :math:`p\texttt{.end}` if :math:`a` is present and not scheduled as
   the first activity on :math:`r`, and :math:`p` is the previous
   activity of :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::EndOfPrevious(
            sequentialResource,  ! (input) an expression
            scheduledActivity,   ! (input) an expression
            firstValue,          ! (optional) an expression
            absentValue          ! (optional) an expression
    )

Arguments
---------

    *sequentialResource*
        An expression that results in a sequential resource.

    *scheduledActivity*
        An expression that results in an activity.

    *firstValue*
        An optional expression that results in an element in the problem
        schedule domain. The default of this expression is the first element in
        the schedule domain of the sequential resource.

    *absentValue*
        An optional expression that results in an element in the problem
        schedule domain. The default of this expression is the first element in
        the problem schedule domain.

Return Value
------------

    This function returns an element in the problem schedule domain.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfPrevious` and :aimms:func:`cp::EndOfNext`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
