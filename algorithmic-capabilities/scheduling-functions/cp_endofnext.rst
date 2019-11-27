.. aimms:function:: cp::EndOfNext(sequentialResource, scheduledActivity, lastValue, absentValue)

.. _cp::EndOfNext:

cp::EndOfNext
=============

The function :aimms:func:`cp::EndOfNext` refers to the end of the next activity in
a sequence of activities. For a resource :math:`r`, an activity
:math:`a`, timeslots :math:`l` and :math:`d`, the function
``cp::EndOfNext(r,a,l,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`l` if :math:`a` is present and scheduled as the last activity
   on :math:`r`, and

-  :math:`n\texttt{.end}` if :math:`a` is present and not scheduled as
   the last activity on :math:`r`, and :math:`n` is the next activity of
   :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::EndOfNext(
            sequentialResource,  ! (input) an expression
            scheduledActivity,   ! (input) an expression
            lastValue,           ! (optional) an expression
            absentValue          ! (optional) an expression
    )

Arguments
---------

    *sequentialResource*
        An expression that results in a sequential resource.

    *scheduledActivity*
        An expression that results in an activity.

    *lastValue*
        An optional expression that results in an element in the problem
        schedule domain. The default value of this expression is the last
        element in the schedule domain of the sequential resource.

    *absentValue*
        An optional expression that results in an element in the problem
        schedule domain. The default value of this expression is the first
        element in the problem schedule domain.

Return Value
------------

    This function returns an element in the problem schedule domain.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfNext` and :aimms:func:`cp::EndOfPrevious`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
