.. aimms:function:: cp::GroupOfPrevious(sequentialResource, scheduledActivity, firstValue, absentValue)

.. _cp::GroupOfPrevious:

cp::GroupOfPrevious
===================

The function :aimms:func:`cp::GroupOfPrevious` refers to the group of the previous
activity in a sequence of activities. The group of an activity is
specified in the ``group definition`` attribute of the sequential
resource to ensure the sequencing. For a resource :math:`r`, an activity
:math:`a`, groups :math:`f` and :math:`d`, the function
``cp::GroupOfPrevious(r,a,f,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`f` if :math:`a` is present and scheduled as the first activity
   on :math:`r`, and

-  :math:`GroupOf(r,p)` if :math:`a` is present and not scheduled as the
   first activity on :math:`r`, and :math:`p` is the previous activity
   of :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::GroupOfPrevious(
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
        An optional expression that results in a group. The default value of
        this expression is the first element of the group set of the sequential
        resource.

    *absentValue*
        An optional expression that results in a group. The default value of
        this expression is the first element of the group set of the sequential
        resource.

Return Value
------------

    This function returns a group.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfPrevious` and :aimms:func:`cp::EndOfNext`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
