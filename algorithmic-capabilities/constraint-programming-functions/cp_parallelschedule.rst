.. aimms:function:: cp::ParallelSchedule(resourceCapacity, jobBinding, jobBegin, jobDuration, jobEnd, jobWeight)

.. _cp::ParallelSchedule:

cp::ParallelSchedule
====================

The function ``cp::ParallelSchedule(c,j,s_j,d_j,e_j,w_j)`` models a
resource that can handle multiple jobs :math:`j` at the same time. The
capacity of the resource is :math:`c` units. The job :math:`j` starts at
period :math:`s_j` and is active up to but not including period
:math:`e_j`, during :math:`d_j` periods. Job :math:`j` requires (a
weight of) :math:`w_j` units of the resource.

Mathematical Formulation
------------------------

    ``cp::ParallelSchedule(c,j,s_j,d_j,e_j,w_j)`` is equivalent to

    .. math:: \begin{array}{l} \forall t: \sum_{j|s_j\leq{}t<e_j} w_j\leq c \\ \forall j: s_j + d_j = e_j. \end{array}

Function Prototype
------------------

    .. code-block:: aimms

            cp::ParallelSchedule(
                resourceCapacity,  ! (input) an expression
                jobBinding,        ! (input) an index binding
                jobBegin,          ! (input/output) an expression
                jobDuration,       ! (input/output) an expression
                jobEnd,            ! (input/output) an expression
                jobWeight          ! (input/output) an expression 
            )

Arguments
---------

    *resourceCapacity*
        This argument is the capacity that the single resource has available to
        handle multiple jobs at the same time. It is a integer valued expression
        and the unit of measurement of this expression should be commensurate to
        the unit of measurement of ``jobWeight``. This expression may not
        involve variables.

    *jobBinding*
        The index binding that specifies the jobs that need to be scheduled.

    *jobBegin*
        An expression that involves variables. When this function is used in a
        constraint definition it should involve variables. The result is a
        vector with an element for each possible value of the indices in
        ``jobBinding``. This argument is integer or element valued, i.e. no
        string, fractional or unit values.

    *jobDuration*
        An expression that may involve variables. The result of this expression
        is an integer non-negative value. The result is a vector with an element
        for each possible value of the indices in ``jobBinding``. This argument
        is integer valued, i.e. no element, string, fractional or unit values,
        but elements from the set ``Integers`` are allowed.

    *jobEnd*
        An expression that involves variables. When this function is used in a
        constraint definition it should involve variables. This expression has
        the same data type as ``jobBegin``. The result is a vector with an
        element for each possible value of the indices in ``jobBinding``. This
        argument is integer or element valued, i.e. no string, fractional or
        unit values.

    *jobWeight*
        An expression that may involve variables. The result of this expression
        is an integer non-negative value. The unit of measurement of this
        expression is commensurate with the unit of measurement of
        ``lowerLimit`` and ``upperLimit``. The result is a vector with an
        element for each possible value of the indices in ``jobBinding``. This
        argument is integer valued, i.e. no element, string, fractional or unit
        values, but elements from the set ``Integers`` are allowed.

This argument is integer or element valued, i.e. no string, fractional
or unit values.

Return Value
------------

    This function returns 1 if the jobs can be scheduled within the resource
    limits. If the index domain argument ``jobBinding`` is empty, this
    function also returns 1. Otherwise it returns 0.

.. note::

    -  The arguments of this function involve discrete AIMMS variables and
       AIMMS parameters, not AIMMS activities.

    -  This and similar constraints are also known in the Constraint
       Programming literature as ``Cumulative`` constraints.

.. seealso::

    -  The examples at the function :aimms:func:`cp::AllDifferent` illustrate how the index
       binding and vector arguments are used.

    -  Chapter 22 on Constraint Programming in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The `Global Constraint Catalog <https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/>`__, which
       references this function as ``cumulative``.
