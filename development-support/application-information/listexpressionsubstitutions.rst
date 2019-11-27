.. aimms:procedure:: ListExpressionSubstitutions()

.. _ListExpressionSubstitutions:

ListExpressionSubstitutions
===========================

With the procedure :aimms:func:`ListExpressionSubstitutions`, the expressions
substituted are printed to the listing file.

.. code-block:: aimms

    ListExpressionSubstitutions()

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

Example
-------

    With the definition: 

    .. code-block:: aimms

            Parameter Conn3 {
                IndexDomain  :  (l1,l4);
                Definition   : {
                    1 | sum( (l2,l3) | d(l1,l2) <= md and
                                       d(l2,l3) <= md and
                                       d(l3,l4) <= md
                                       ,1 )
                }
           }

    The procedure
    :aimms:func:`ListExpressionSubstitutions` will print to the listing file:

    .. code-block:: aimms

          1: D(l1,l2) <= md has card 0, and is used 1 times
          2: D(l2,l3) <= md has card 0, and is used 1 times
          3: D(l3,l4) <= md has card 0, and is used 1 times

    The card is the number of elements in the cache, here 0;
    when running this example, the definition of Conn3 was not evaluated,
    and the procedure :aimms:func:`ListExpressionSubstitutions` does not force the
    evaluation of the caches either.
