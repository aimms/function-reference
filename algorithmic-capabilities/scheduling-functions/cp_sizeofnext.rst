.. aimms:function:: cp::SizeOfNext(sequentialResource, scheduledActivity, lastValue, absentValue)

.. _cp::SizeOfNext:

cp::SizeOfNext
==============

The function :aimms:func:`cp::SizeOfNext` refers to the size of the next activity
in a sequence of activities. A size is an integer in the range
:math:`\{0..card(\texttt{problem schedule domain})-1\}`. For a resource
:math:`r`, an activity :math:`a`, sizes :math:`l` and :math:`d`, the
function ``cp::SizeOfNext(r,a,l,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`l` if :math:`a` is present and scheduled as the last activity
   on :math:`r`, and

-  :math:`n\texttt{.size}` if :math:`a` is present and not scheduled as
   the last activity on :math:`r`, and :math:`n` is the next activity of
   :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::SizeOfNext(
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
        An optional expression that results in a size. The default value of this
        expression is 0.

    *absentValue*
        An optional expression that results in a size. The default value of this
        expression is 0.

Return Value
------------

    This function returns a size.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfNext` and :aimms:func:`cp::EndOfPrevious`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
