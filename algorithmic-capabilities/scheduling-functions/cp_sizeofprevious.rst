.. aimms:function:: cp::SizeOfPrevious(sequentialResource, scheduledActivity, firstValue, absentValue)

.. _cp::SizeOfPrevious:

cp::SizeOfPrevious
==================

The function :aimms:func:`cp::SizeOfPrevious` refers to the size of the previous
activity in a sequence of activities. A size is an integer in the range
:math:`\{0..card(\texttt{problem schedule domain})-1\}`. For a resource
:math:`r`, an activity :math:`a`, sizes :math:`f` and :math:`d`, the
function ``cp::SizeOfPrevious(r,a,f,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`f` if :math:`a` is present and scheduled as the first activity
   on :math:`r`, and

-  :math:`p\texttt{.size}` if :math:`a` is present and not scheduled as
   the first activity on :math:`r`, and :math:`p` is the previous
   activity of :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::SizeOfPrevious(
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
        An optional expression that results in a size. The default of this
        expression is 0.

    *absentValue*
        An optional expression that results in a size. The default of this
        expression is 0.

Return Value
------------

    This function returns a size.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfPrevious` and :aimms:func:`cp::EndOfNext`.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
