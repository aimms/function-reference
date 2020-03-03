.. aimms:function:: cp::Cardinality(inspectedBinding, inspectedValues, lookupValueBinding, lookupValues, numberOfOccurrences, occurrenceLimit)

.. _cp::Cardinality:

cp::Cardinality
===============

The function :aimms:func:`cp::Cardinality` can be used to restrict the number of
occurrences of a particular value in (a slice of) an indexed identifier
or expression. This function is typically used in constraints that
enforce selected values a limited number of times. The function
:aimms:func:`cp::Cardinality` counts the number of occurrences of a collection of
values and either ensures that the number of occurrences is within
bounds, or sets this equal to the value of a variable.

Mathematical Formulation
------------------------

    The function ``cp::Cardinality(i,x_i,j,c_j,y_j[,u_j])`` returns 1 if the
    number of occurrences where :math:`x_i` equals :math:`c_j` is equal to
    :math:`y_j` or in the range {:math:`y_j`..\ :math:`u_j`}for all
    :math:`j`. ``cp::Cardinality(i,x_i,j,c_j,y_j)`` is equivalent to

    .. math:: \forall j: \sum_i (x_i=c_j) = y_j

    \ and ``cp::Cardinality(i,x_i,j,c_j,l_j,u_j)`` is equivalent to

    .. math:: \forall j: l_j \leq \sum_i (x_i=c_j) \leq u_j

Function Prototype
------------------

    .. code-block:: aimms

        cp::Cardinality(
                inspectedBinding,    ! (input) an index binding
                inspectedValues,     ! (input) an expression
                lookupValueBinding,  ! (input) an index binding
                lookupValues,        ! (input) an expression
                numberOfOccurrences, ! (input/output) an expression
                occurrenceLimit)     ! (optional/input) an expression

Arguments
---------

    *inspectedBinding*
        An index binding that specifies and possibly limits the scope of
        indices. This argument follows the syntax of the index binding argument
        of iterative operators.

    *inspectedValues*
        An expression that may involve variables, but can only contain integer
        or element values (i.e. no strings, fractional or unit values). The
        result is a vector with an element for each possible value of the
        indices according to ``inspectedBinding``.

    *lookupValueBinding*
        An index binding that specifies and possibly limits the scope of
        indices. This argument follows the syntax of the index binding argument
        of iterative operators.

    *lookupValues*
        An expression that does not involve variables. The result is a vector
        with an element for each possible value of the indices according to
        ``lookupValueBinding``.

    *numberOfOccurrences*
        An expression that may involve variables. The result is a vector with an
        element for each possible value of the indices according to
        ``lookupValueBinding``.

    *occurrenceLimit*
        An optional expression that does not involve variables. The result is a
        vector with an element for each possible value of the indices according
        to ``lookupValueBinding``. In addition, if this argument is specified,
        the argument ``numberOfOccurrences`` is not allowed to contain variables
        either.

Return Value
------------

    This function returns 1 if the above condition is met. Also if the index
    binding argument ``lookupValueBinding`` is empty, this function will
    return 1.

Example
-------

    In car sequencing the next constraint ensures that the demand
    ``nbCarsPerClass( c )`` for each class ``c`` of type ``car(i)`` is met.
    The value of element variable ``car`` is a class of car. 

    .. code-block:: aimms

                Constraint meetDemand {
                    Definition   : {
                        cp::Cardinality(
                             inspectedBinding    :  i, 
                             inspectedValues     :  car(i), 
                             lookupValueBinding  :  c, 
                             lookupValues        :  c, 
                             numberOfOccurrences :  nbCarsPerClass( c ), 
                             occurrenceLimit     :  nbCars)
                    }
                }

.. seealso::

    -  The functions :aimms:func:`cp::Count` and :aimms:func:`cp::Sequence`.

    -  The Chapter on Constraint Programming 22 in the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.

    -  The `Global Constraint Catalog <https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/>`__, which
       references this function as ``global_cardinality``.
