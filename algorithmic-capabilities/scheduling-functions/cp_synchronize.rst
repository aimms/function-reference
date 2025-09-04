.. aimms:function:: cp::Synchronize(globalActivity, activityBinding, subActivity)

.. _cp::Synchronize:

cp::Synchronize
===============

The function ``cp::Synchronize(g,i,a_i)`` returns 1 if activity
:math:`g` is not present, or if all present activities :math:`a_i` match
activity :math:`g`. The function ``cp::Synchronize(g,i,a_i)`` is
equivalent to

.. math:: g\texttt{.Present} \Rightarrow \forall i| a_i\texttt{.Present}: \left\{ \begin{array}{l} g\texttt{.Begin} = a_i\texttt{.Begin} \\ g\texttt{.End} = a_i\texttt{.End} \end{array} \right.

\ This function is typically used in scheduling problems to synchronize
activities.

.. code-block:: aimms

    cp::Synchronize(
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
    otherwise. When the index domain ``activityBinding`` is empty this
    function will return an error.

.. seealso::

    - The functions :aimms:func:`cp::Alternative` and :aimms:func:`cp::Span`.
