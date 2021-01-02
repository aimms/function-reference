.. aimms:function:: cp::Sequence(inspectedBinding, inspectedValues, lookupValues, sequenceLength, lowerBound, upperBound, cyclic)

.. _cp::Sequence:

cp::Sequence
============

The function :aimms:func:`cp::Sequence` is used to limit the number of occurrences
of a group of values in each contiguous sequence of a row of variables.
It is used to model that some values may occur only a limited number of
times in a contiguous subset of the variables.

Mathematical Formulation
------------------------

    The function ``cp::Sequence(i,x_i,S,q,l,u[,c])`` returns 1 if, for each
    contiguous sequence of length :math:`q`, the number of times that
    :math:`x_i` is in :math:`S` is within the range :math:`\{ l .. u\}`.
    ``cp::Sequence(i,x_i,S,q,l,u,c)`` is equivalent to

    .. math:: \begin{array}{llll} \forall i=1..n-q+1: & l \leq \sum_{j=0}^{q-1} (x_{i+j}\in S) & \leq u & c=0 \\ \forall i=1..n : & l \leq \sum_{j=0}^{q-1} (x_{(i+j-1)\%n+1}\in S) & \leq u & c\neq 0 \\ \end{array}

Function Prototype
------------------

    .. code-block:: aimms

            cp::Sequence(
                inspectedBinding, ! (input) an index binding
                inspectedValues,  ! (input/output) an expression
                lookupValues,     ! (input) a set valued expression
                sequenceLength,   ! (input) an expression
                lowerBound,       ! (input) an expression 
                upperBound,       ! (input) an expression 
                cyclic            ! (optional, input) an expression
            )

Arguments
---------

    *inspectedBinding*
        The index binding for which the ``inspectedValues`` expression should be
        inspected on occurences of values in the ``lookupValues`` set.

    *inspectedValues*
        The expression indexed over ``inspectedBinding`` for which the number of
        occurrences of the values in ``lookupValues`` is limited per
        subsequence. This expression may involve variables, but can only contain
        integer or element values (i.e. no strings, fractional or unit values).

    *lookupValues*
        The set containing the particular values that should occur only a
        limited number of times in each subsequence. This set valued expression
        should be a subset of the range of ``inspectedValues`` and does not
        involve variables.

    *sequenceLength*
        The sequence length. An expression that does not involve variables. This
        argument should be in the range
        :math:`\{1..\texttt{card}(\texttt{range}(\texttt{inspectedValues}))\}`.

    *lowerBound*
        The lower bound on the number of occurences. This expression does not
        involve variables. This argument should be in the range
        :math:`\{0..\texttt{upperBound}\}`.

    *upperBound*
        The upper bound on the number of occurences. This expression does not
        involve variables. This argument should be in the range
        :math:`\{\texttt{lowerBound}..\texttt{sequenceLength}\}`.

    *cyclic*
        An optional expression that indicates whether cyclic subsequences should
        also be inspected. E.g. when you have a set 1,2,3,4,5 then 4,5,1 is a
        cyclic subsequence of length 3. The ``cyclic`` expression cannot involve
        variables and the default of this argument is 0.

Return Value
------------

    This function returns 1 if the above condition is met.

Example
-------

    In car sequencing the constraint below ensures that no more ``car``\ s
    of class ``c`` with option ``o`` are built in a sequence of length
    ``blockSize(o)`` than ``maxCarsPerBlock(o)``. Here, the indexed set
    ``classesHavingOption(o)`` is, for each option ``o``, the classes of car
    that have that option. 

    .. code-block:: aimms

                Constraint respectCapacity {
                    IndexDomain  : (o);
                    Definition   : {
                        cp::Sequence(
                            inspectedBinding :  i,
                            inspectedValues  :  car(i),
                            lookupValues     :  classesHavingOption(o),
                            sequenceLength   :  blockSize(o),
                            lowerBound       :  0,
                            upperBound       :  maxCarsPerBlock(o) )
                    }
                }

    In crew scheduling the constraint
    below ensures that after a flight an attendant ``att`` has at least two
    days off (works at most one day in each sequence of three days). The
    value ``1`` is converted to the set ``{1}`` by AIMMS. 

    .. code-block:: aimms

                Constraint AssureDaysOff {
                    IndexDomain  : (att);
                    Definition   : {
                         cp::Sequence(
                             inspectedBinding :  f,
                             inspectedValues  :  CrewOnFlight(att, f),
                             lookupValues     :  1,
                             sequenceLength   :  3,
                             lowerBound       :  0,
                             upperBound       :  1,
                             cyclic           :  1)
                    }
               }

.. seealso::

    -  The functions :aimms:func:`cp::Count` and :aimms:func:`cp::Cardinality`.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The `Global Constraint Catalog <https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/titlepage.html>`__, which
       references this function as ``among_seq``.
