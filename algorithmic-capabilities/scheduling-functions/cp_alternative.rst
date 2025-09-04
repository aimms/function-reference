.. aimms:function:: cp::Alternative(globalActivity, activityBinding, subActivity, noSelected)

.. _cp::Alternative:

cp::Alternative
===============

The function ``cp::Alternative(g,i,a_i,n)``, returns

-  if activity :math:`g` is not present, the value 1 if none of the
   activities :math:`a_i` are present and 0 otherwise.

-  if activity :math:`g` is present, the value 1 if precisely :math:`n`
   activities :math:`a_i` are present and these present activities match
   the activity :math:`g`.

The function ``cp::Alternative(g,i,a_i,n)`` is equivalent to

.. math:: g\texttt{.Present} = 0 \Leftrightarrow \forall i: a_i\texttt{.Present} = 0

\ and

.. math:: g\texttt{.Present} = 1 \Leftrightarrow \left\{ \begin{array}{l} \sum_i a_i\texttt{.Present} = n \\ \forall i: a_i\texttt{.Present} \Rightarrow \left\{ \begin{array}{l} g\texttt{.Begin} = a_i\texttt{.Begin} \\ g\texttt{.End} = a_i\texttt{.End} \end{array} \right. \end{array} \right.

This function is typically used in scheduling problems to denote
selected (matching) activities.

.. code-block:: aimms

    cp::Alternative(
            globalActivity,   ! (input) an expression 
            activityBinding,  ! (input) an activity binding
            subActivity,      ! (input) an expression
            noSelected        ! (optional) an expression
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

    *noSelected*
        The number of alternatives, the default being 1. This expression may
        involve variables.

Return Value
------------

    This function returns 1 if the above condition is satisfied, or
    otherwise 0. When the index domain ``activityBinding`` is empty this
    function will return an error.

Example
-------

In the example below we require precisely one of the activities
``altAct(i)`` to match the activity ``chosenAct(i)``. 

.. code-block:: aimms

    Constraint PreciselyOneAlternativeMatches {
        Definition   :  cp::Alternative( chosenAct, i, altAct(i) );
    }

We could change the above example to allow multiple matches as follows:

.. code-block:: aimms

    Variable noMatches {
        Range        :  {
            { 1 .. n }
        }
    }
    Constraint AtLeastOneAlternativeMatches {
        Definition   :  cp::Alternative( chosenAct, i, altAct(i), noMatches );
    }

Here, the number of matches is counted in the integer
variable ``noMatches``.

.. seealso::

    - The functions :aimms:func:`cp::Span` and :aimms:func:`cp::Synchronize`.
