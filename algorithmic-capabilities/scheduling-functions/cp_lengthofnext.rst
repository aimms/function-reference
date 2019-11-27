.. aimms:function:: cp::LengthOfNext(sequentialResource, scheduledActivity, lastValue, absentValue)

.. _cp::LengthOfNext:

cp::LengthOfNext
================

The function :aimms:func:`cp::LengthOfNext` refers to the length of the next
activity in a sequence of activities. A length is an integer in the
range :math:`\{0..card(\texttt{problem schedule domain})-1\}`. For a
resource :math:`r`, an activity :math:`a`, lengths :math:`l` and
:math:`d`, the function ``cp::LengthOfNext(r,a,l,d)`` returns

-  :math:`d` if :math:`a` is absent,

-  :math:`l` if :math:`a` is present and scheduled as the last activity
   on :math:`r`, and

-  :math:`n\texttt{.length}` if :math:`a` is present and not scheduled
   as the last activity on :math:`r`, and :math:`n` is the next activity
   of :math:`a` scheduled on :math:`r`.

.. code-block:: aimms

    cp::LengthOfNext(
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
        An optional expression that results in a length. The default value of
        this expression is 0.

    *absentValue*
        An optional expression that results in a length. The default value of
        this expression is 0.

Return Value
------------

    This function returns a length.

.. seealso::

    -  The functions :aimms:func:`cp::BeginOfNext` and :aimms:func:`cp::EndOfPrevious`, and

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
