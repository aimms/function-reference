.. aimms:function:: cp::GroupOfNext(sequentialResource, scheduledActivity, lastValue, absentValue)

.. _cp::GroupOfNext:

cp::GroupOfNext
===============

The function :aimms:func:`cp::GroupOfNext` refers to the group of the next
activity in a sequence of activities. The group of an activity is
specified in the ``group definition`` attribute of the sequential
resource to ensure the sequencing. For a resource :math:`r`, an activity
:math:`a`, groups :math:`l` and :math:`d`, the function
``cp::GroupOfNext(r,a,l,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`l` if :math:`a` is present and scheduled as the last activity
   on :math:`r`, and

-  :math:`GroupOf(r,n)` if :math:`a` is present and not scheduled as the
   last activity on :math:`r`, and :math:`n` is the next activity of
   :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::GroupOfNext(
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
        An optional expression that results in a group. The default value of
        this expression is the last element in the group set of the sequential
        resource.

    *absentValue*
        An optional expression that results in a group. The default value of
        this expression is the last element in the group set of the sequential
        resource.

Return Value
------------

    This function returns a group.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfNext` and :aimms:func:`cp::EndOfPrevious`.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
