.. aimms:function:: cp::BeginOfPrevious(sequentialResource, scheduledActivity, firstValue, absentValue)

.. _cp::BeginOfPrevious:

cp::BeginOfPrevious
===================

The function :aimms:func:`cp::BeginOfPrevious` refers to the begin of the previous
activity in a sequence of activities. For a resource :math:`r`, an
activity :math:`a`, timeslots :math:`l` and :math:`d`, the function
``cp::BeginOfNext(r,a,l,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`l` if :math:`a` is present and scheduled as the first activity
   on :math:`r`, and

-  :math:`p\texttt{.begin}` if :math:`a` is present and not scheduled as
   the last activity on :math:`r`, and :math:`p` is the previous
   activity of :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::BeginOfPrevious(
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
        schedule domain. The default value of this expression is the first
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

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
