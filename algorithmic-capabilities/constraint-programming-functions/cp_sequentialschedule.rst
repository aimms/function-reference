.. aimms:function:: cp::SequentialSchedule(jobBinding, jobBegin, jobDuration, jobEnd)

.. _cp::SequentialSchedule:

cp::SequentialSchedule
======================

The function ``cp::SequentialSchedule(j,s_j,d_j,e_j)`` models a resource
that can handle only one job at a time. A job :math:`j` is scheduled
from start time :math:`s_j` until, but not including, end time
:math:`e_j` and over a number of periods :math:`d_j`. This function
returns 1 if the jobs are scheduled such that no two jobs overlap.

Mathematical Formulation
------------------------

    ``cp::SequentialSchedule(j,s_j,d_j,e_j)`` is equivalent to

    .. math:: \begin{array}{l} \forall i,j,i \neq j: (s_i+d_i\leq s_j) \vee (s_j + d_j \leq s_i) \\ \forall j: s_j + d_j = e_j \end{array}

Function Prototype
------------------

    .. code-block:: aimms

        cp::SequentialSchedule(
                jobBinding,  ! (input) an index binding
                jobBegin,    ! (input) an expression
                jobDuration, ! (input) an expression
                jobEnd       ! (input) an expression
        )

Arguments
---------

    *jobBinding*
        An index binding that specifies and possibly limits the scope of
        indices. This argument follows the syntax of the index binding argument
        of iterative operators.

    *jobBegin*
        An expression that involves variables. The result is a vector with an
        element for each possible value of the indices in ``jobBinding``.

    *jobDuration*
        An expression that may involve variables. The result of this expression
        is an integer non-negative value. The result is a vector with an element
        for each possible value of the indices in ``jobBinding``.

    *jobEnd*
        An expression that involves variables. This expression has the same data
        type as ``jobBegin``. The result is a vector with an element for each
        possible value of the indices in ``jobBinding``.

Return Value
------------

    This function returns 1 if the jobs can be scheduled such that no two
    jobs overlap. If the index binding argument ``job`` is empty, this
    function will return 1. Otherwise it returns 0.

.. note::

    -  The arguments to this function involve discrete AIMMS variables and
       AIMMS parameters, not AIMMS activities.

    -  This and similar constraints are also known in the Constraint
       Programming literature as ``unary`` or ``disjunctive`` constraints.

Example
-------

    The following example models the intuitive idea that with an increase in
    the size of a task also the time window in which that task is to be
    executed increases. 

    .. code-block:: aimms

                Parameter nrTasks {
                    Definition   :  10;
                }
                Parameter smallestWidth {
                    Definition   :  4;
                }
                Set tasks {
                    Index        :  t;
                    Definition   :  elementrange( 1, nrTasks, 1, 'task');
                }
                Parameter release {
                    IndexDomain  :  (t);
                    Definition   :  Ord(t);
                }
                Parameter deadline {
                    IndexDomain  :  (t);
                    Definition   :  2*nrTasks-Ord(t)+smallestWidth;
                }
                Parameter processingTime {
                    IndexDomain  :  (t);
                    Definition   :  ceil(0.125*(deadline(t) - release(t)));
                }
                Variable startTime {
                    IndexDomain  :  (t);
                    Range        :  {
                        {release(t) .. deadline(t)}
                    }
                }
                Variable endTime {
                    IndexDomain  :  (t);
                    Range        :  {
                        {release(t) .. deadline(t)}
                    }
                }
                Constraint UnaryResource {
                    Definition   : {
                        cp::SequentialSchedule(t, startTime(t),
                            processingTime(t), endTime(t))
                    }
                }

    This leads to the following results
    (extracted from the listing file): 

    .. code-block:: aimms

                    name                    lower    level    upper
                    startTime('task01')         1        1       23
                    startTime('task02')         2       18       22
                    startTime('task03')         3       15       21
                    startTime('task04')         4        4       20
                    startTime('task05')         5       13       19
                    startTime('task06')         6        6       18
                    startTime('task07')         7       11       17
                    startTime('task08')         8        8       16
                    startTime('task09')         9        9       15
                    startTime('task10')        10       10       14
                    endTime('task01')           1        4       23
                    endTime('task02')           2       21       22
                    endTime('task03')           3       18       21
                    endTime('task04')           4        6       20
                    endTime('task05')           5       15       19
                    endTime('task06')           6        8       18
                    endTime('task07')           7       13       17
                    endTime('task08')           8        9       16
                    endTime('task09')           9       10       15
                    endTime('task10')          10       11       14

    The following Gantt chart
    illustrates that the solution satisfies the restricition imposed by
    :aimms:func:`cp::SequentialSchedule`.

    .. figure:: Gantt-Chart-Example-Sequential-Schedule.jpg
       :name: fig:sequential-schedule-narrowing-gantt-chart

       Gantt chart for solution of :aimms:func:`cp::SequentialSchedule`

.. seealso::

    -  The examples at the function :aimms:func:`cp::AllDifferent` illustrate how the index
       binding and vector arguments are used.

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The global constraint catalog
       http://www.emn.fr/z-info/sdemasse/gccat/Cdisjunctive.html which
       references this function as ``disjunctive``.
