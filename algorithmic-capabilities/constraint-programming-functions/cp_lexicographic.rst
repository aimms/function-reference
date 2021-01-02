.. aimms:function:: cp::Lexicographic(valueBinding, firstValues, secondValues, allowEqual)

.. _cp::Lexicographic:

cp::Lexicographic
=================

The function :aimms:func:`cp::Lexicographic` ensures that the data of one
expression comes lexicographically (i.e. according to the set order)
before another expression. This function is often used to reduce
symmetry in two variables.

Mathematical Formulation
------------------------

    ``cp::Lexicographic(k,x_k,y_k[,e])`` is equivalent to

    .. math:: \exists i \in \{1..n\} : (\forall j: j < i: x_j=y_j)\wedge \left\{ \begin{array}{ll} x_i<y_i & \textrm{if } e = 0 \\ x_i\leq y_i & \textrm{if } e \neq 0 \\ \end{array} \right.

    \ where :math:`n` equals ``card(range(k))``.

Function Prototype
------------------

    .. code-block:: aimms

           cp::Lexicographic(
                valueBinding, ! (input) an index binding
                firstValues,  ! (input/output) an expression
                secondValues, ! (input/output) an expression 
                allowEqual    ! (optional input) an expression
           )

Arguments
---------

    *valueBinding*
        The index binding over which the next two arguments are defined.

    *firstValues*
        The expression that should lexicographically come before
        ``secondValues``. It is defined over index binding ``valueBinding`` and
        may involve variables.

    *secondValues*
        The expression that should lexicographically come after ``firstValues``.
        It is defined over index binding ``valueBinding`` and may involve
        variables.

    *allowEqual*
        When this optional argument is specified and non-zero, the expressions
        ``firstValues`` and ``secondValues`` are allowed to be equal. The
        ``allowEqual`` expression may not involve variables. The default of this
        argument is 0.

Return Value
------------

    This function returns 1 if the above condition is met. When the index
    binding ``valueBinding`` is empty, this function returns

    -  0 if allowEqual is 0

    -  1 if allowEqual is not 1.

.. note::

    Please note that the comparison between the two expressions is done,
    based on the complete specified index binding and not pair-wise for
    every element in that index domain.

Example
-------

    The constraint ``x_before_y`` ensures that the identifier ``x`` comes
    lexicographically before the identifier ``y``. 

    .. code-block:: aimms

                Constraint x_before_y {
                    Definition   :  cp::Lexicographic( i, x(i), y(i) );
                }

    Suppose

    .. code-block:: aimms

            x = data { 'a1' : 1, 'a2' : 2, 'a3' : 2 }
            y = data { 'a1' : 1, 'a2' : 3, 'a3' : 1 }

    Then the constraint ``x_before_y`` is met. Please note that
    in the case of 'a3', ``x = 2`` and ``y = 1``. Allthough 2 does not come
    lexicographically before 1, the constraint *is* met. The ordering is
    based on the *whole* index domain, and not 'pair wise'. Because for 'a2'
    2 comes lexicographically before 3, the ``x``- and ``y``-values for 'a3'
    are irrelevant here. Higher dimensional variables can also be compared
    using cp::Lexicographic as is illustrated next. Consider the following
    declarations: 

    .. code-block:: aimms

            Set S {
                Index        :  i, j;
                InitialData  :  data { a, b, c };
            }
            Variable X {
                IndexDomain  :  (i,j);
                Range        :  binary;
            }
            Variable Y {
                IndexDomain  :  (i,j);
                Range        :  binary;
            }
            Constraint xylex {
                Definition   : {
                    cp::Lexicographic(
                        (i,j)|ord(i)<=ord(j),
                        x(i,j), y(i,j))
                }
            }

    Instantiated constraints are presented in the
    constraint listing. For the constraint ``xylex`` this looks as follows:

    .. code-block:: aimms

        ----  xylex

        xylex .. [ 1 | 1 | after ]

            cp::Lexicographic({X(a,a), X(a,b), X(a,c), X(b,b), X(b,c), X(c,c)},
                              {Y(a,a), Y(a,b), Y(a,c), Y(b,b), Y(b,c), Y(c,c)},
                  allowEqual: 0)

            name    lower level upper
            X(a,a)      0     0     1
            X(a,b)      0     0     1
            X(a,c)      0     0     1
            X(b,b)      0     0     1
            X(b,c)      0     0     1
            X(c,c)      0     0     1
            Y(a,a)      0     1     1
            Y(a,b)      0     0     1
            Y(a,c)      0     0     1
            Y(b,b)      0     0     1
            Y(b,c)      0     0     1
            Y(c,c)      0     0     1

    Here AIMMS visits all elements of the two dimensional
    variables ``x`` and ``y``, by varying the indices ``i`` and ``j`` in the
    index binding ``(i,j)`` and adhering to the index domain condition
    ``ord(i)<=ord(j)``. In the index binding ``(i,j)`` the index ``j`` comes
    after the index ``i`` and thus the index ``j`` is varied more.

.. seealso::

    -  The help text associated with the option ``constraint_listing``. This
       option can be found via the AIMMS menu ``settings`` > ``project options`` category ``Solvers general`` > ``Standard reports`` > ``constraints``.

    -  :doc:`optimization-modeling-components/constraint-programming/index` on Constraint Programming in the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The `Global Constraint Catalog <https://web.imt-atlantique.fr/x-info/sdemasse/gccatold/>`__, which
       references this function as ``lex_less`` and ``lex_lesseq``.
