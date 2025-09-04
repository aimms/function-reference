.. aimms:function:: cp::BinPacking(binBinding, binCapacity, objectBinding, objectAssignment, objectWeight[, numberOfBinsUsed])

.. _cp::BinPacking:

cp::BinPacking
==============

This function is used to model the assignment of objects in bins: a set
of objects, each with its own known 'weight', is to be placed into a set
of bins, each with its own known capacity.

Mathematical Formulation
------------------------

The function ``cp::BinPacking(b,c_b,o,a_o,w_o[,u])`` returns 1, if, for
each bin :math:`b`, the sum of objects :math:`o` placed, according to
assignment variable :math:`a_o`, into bin :math:`b` (:math:`a_o=b`) of
weight :math:`w_o`, is less than or equal to the capacity :math:`c_b`.
In addition, if the argument :math:`u` is specified, the number of
non-empty (i.e. used) bins is set equal to :math:`u`.
``cp::BinPacking(b,c_b,o,a_o,w_o[,u])`` is equivalent to

.. math:: \forall b: \sum_{o \mid a_o = b} w_o \otimes c_b \textrm{ where } \left\{ \begin{array}{ll} \otimes \textrm{ is } = & \textrm{if } c_b \textrm{ involves variables} \\ \otimes \textrm{ is } \leq & \textrm{if } c_b \textrm{ does not involve variables} \end{array} \right.

\ If argument :math:`u` is present, the following constraint also
applies.

.. math:: u = \sum_{b \mid c_b } 1

Function Prototype
------------------

.. code-block:: aimms

    cp::BinPacking(
            binBinding,       ! (input) an index binding
            binCapacity,      ! (input/output) an expression
            objectBinding,    ! (input) an index binding
            objectAssignment, ! (input/output) an expression
            objectWeight,     ! (input) an expression 
            numberOfBinsUsed  ! (optional, input/output) an expression
    )

Arguments
---------

    *binBinding*
        The index binding that specifies the available bins.

    *binCapacity*
        The capacity of the available bins defined over the index binding
        ``binBinding``. This expression may involve variables:

        -  When the ``binCapacity`` expression does not involve variables, it is
           interpreted as an upperbound on the bin capacity.

        -  When the ``binCapacity`` expression involves variables, the
           constraint forces the capacities of the bins to equal this
           expression.

    *objectBinding*
        The index binding that specifies the objects that need to be packed.

    *objectAssignment*
        For each object in ``objectBinding``, ``objectAssignment`` contains a
        bin in ``binBinding`` to indicate that the object is assigned to that
        particular bin. The expression for ``objectAssignment`` may involve
        variables.

    *objectWeight*
        The weight of each object, defined over the binding domain
        ``objectBinding``. This expression cannot involve variables.

    *numberOfBinsUsed (optional)*
        The number of bins that are used to pack the objects. This argument is
        an optional expression with a numerical value that may involve
        variables.

Return Value
------------

    The function returns 1 when the placement of objects into bins is such
    that the capacity of the bins is not exceeded. When the object binding
    argument ``objectBinding`` is empty, this function will return 1. In all
    other cases, the function returns 0.

Example
-------

Let us move 7 benches of size 3, 1, 2, 2, 2, 2, and 3 respectively from
one place to the next over several trips with a single truck. The truck
we are using has a capacity of 5 (in terms of size, not benches). With
the simplest of heuristics, we fill the truck sequentially with these
benches until we have no benches left to fill the truck. This heuristic
leads to the following schedule:

.. table:: 

    ==== ===========
    trip bench sizes
    ==== ===========
    1    3 1
    2    2 2
    3    2 2
    4    3
    ==== ===========

With the aid of :aimms:func:`cp::BinPacking` we can do better. The model is as
follows: 

.. code-block:: aimms

            Set Benches {
                Index        :  bench;
                Definition   :  ElementRange( 1, 7, prefix:"bench-");
            }
            Parameter BenchSize {
                IndexDomain  :  (bench);
                InitialData  : {
                    data { bench-1 : 3, bench-2 : 1, bench-3 : 2, bench-4 : 2, 
                        bench-5 : 2, bench-6 : 2, bench-7 : 3 }
                }
            }
            Parameter TruckSize {
                InitialData :  5;
            }
            Set Trips {
                Index        :  trip;
                Definition   :  ElementRange(1,5,prefix:"trip-");
            }
            ElementVariable BenchTrip {
                IndexDomain  :  bench;
                Range        :  Trips;
            }
            Variable NumberOfTripsNeeded {
                Range        :  free;
            }
            Constraint RespectTruckSize {
                Definition   : {
                    cp::BinPacking(trip, TruckSize, bench, BenchTrip(bench), 
                    BenchSize(bench), NumberOfTripsNeeded)
                }
            }
            MathematicalProgram TripPlanning {
                Objective    :  NumberOfTripsNeeded;
                Direction    :  minimize;
                Constraints  :  AllConstraints;
                Variables    :  AllVariables;
                Type         :  Automatic;
            }

Solving this model will provide the following
(non-unique) result: 

.. code-block:: aimms

        NumberOfTripsNeeded := 3 ;

        BenchTrip := data { bench-1 : trip-3, bench-2 : trip-1, bench-3 : trip-2, 
                            bench-4 : trip-3, bench-5 : trip-1, bench-6 : trip-1, 
                            bench-7 : trip-2 } ;

Which leads to the following schedule:

.. table:: 

    ==== ===========
    trip bench sizes
    ==== ===========
    1    1 2 2
    2    2 3
    3    3 2
    ==== ===========

In the above example, the ``binCapacity`` argument is a parameter,
because ``TruckSize`` has a fixed value. In such a case, ``TruckSize``
is an upperbound. In the example below, the truck needs to be rented and
we can decide on what size it should be. Therefore, ``TruckSize`` (the
``binCapacity`` argument) is a variable. The bounds of that variable are
used to limit the ``TruckSize``. Note that ``TruckSize`` is indexed over
``trip``, because the ``BinPacking`` constraint enforces that the fill
of the truck is equal to this ``TruckSize``. In case ``TruckSize`` is a
scalar, all the trips should be equally loaded, which in practice is not
necessary. The example below only displays the new or changed
identifiers compared with the example above (the constraint remains the
same, but is displayed for clarity). 

.. code-block:: aimms

        Parameter MaximumTruckSize {
            InitialData  :  8;
        }
        Variable TruckSize {
            IndexDomain  :  trip;
            Range        :  {
                {0..MaximumTruckSize}
            }
        }
        Constraint GetTruckSize {
            Definition   : {
                cp::BinPacking( trip, TruckSize(trip), bench, BenchTrip(bench), 
                BenchSize(bench), NumberOfTripsNeeded )
            }
        }

Solving this model
leads to the following (non-unique) result, where the ``TruckSize`` for
the two trips is 7 and 8, so we need to rent a truck of size 8.

.. code-block:: aimms

        NumberOfTripsNeeded := 2 ;

        BenchTrip := data { bench-1 : trip-2, bench-2 : trip-1, bench-3 : trip-2,
                            bench-4 : trip-1, bench-5 : trip-1, bench-6 : trip-1,
                            bench-7 : trip-2 } ;

Which leads to the following schedule:

.. table:: 

    ==== ===========
    trip bench sizes
    ==== ===========
    1    1 2 2 2
    2    3 2 3
    ==== ===========

.. seealso::

    -  The examples of the function :aimms:func:`cp::AllDifferent` that illustrate how the index
       binding and indexed arguments can be used. Further information on
       index binding can be found in :doc:`procedural-language-components/index-binding/index`.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the Language Reference.

    -  The `Global Constraint Catalog <https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/titlepage.html>`__, which
       references this function as ``bin_packing``.
