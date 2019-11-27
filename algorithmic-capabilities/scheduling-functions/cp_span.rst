.. aimms:function:: cp::Span(globalActivity, activityBinding, subActivity)

.. _cp::Span:

cp::Span
========

The function ``cp::Span(g,i,a_i)`` returns 1 if activity :math:`g` and
activities :math:`a_i` are all not present, or if the begin of present
activity :math:`g` is equal to the first present activity :math:`a_i`
and the end of activity :math:`g` is equal to the end of the last
present activity :math:`a_i`. The function ``cp::Span(g,i,a_i)`` is
equivalent to

.. math:: g\texttt{.Present} = 0 \Leftrightarrow \forall i: a_i\texttt{.Present} = 0

\ and

.. math:: g\texttt{.Present} = 1 \Leftrightarrow \left\{ \begin{array}{l} \exists i|a_i\texttt{.Present} \\ g\texttt{.Begin} = \min_{i|a_i\texttt{.Present}} a_i\texttt{.Begin} \\ g\texttt{.End} = \max_{i|a_i\texttt{.Present}} a_i\texttt{.End} \end{array} \right.

This function is typically used in scheduling problems to split an
activity into sub activities.

.. code-block:: aimms

    cp::Span(
            globalActivity,   ! (input) an expression 
            activityBinding,  ! (input) an index domain
            subActivity       ! (input) an expression
    )

Arguments
---------

    *globalActivity*
        An expression resulting in an activity.

    *activityBinding*
        An index domain that specifies and possibly limits the scope of indices.
        This argument follows the syntax of the index domain argument of
        iterative operators.

    *subActivity*
        An expression resulting in an activity. The result is a vector with an
        element for each possible value of the indices in index domain
        ``activityBinding``.

Return Value
------------

    This function returns 1 if the above condition is satisfied, 0
    otherwise. When the index domain ``i`` is empty this function will
    return an error.

.. seealso::

    The functions :aimms:func:`cp::Alternative` and :aimms:func:`cp::Synchronize`.
