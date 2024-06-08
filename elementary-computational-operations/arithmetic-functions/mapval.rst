.. aimms:function:: MapVal(x)

.. _MapVal:

MapVal
======

.. code-block:: aimms

    MapVal(
          x             ! (input) numerical expression
          )

Arguments
---------

    *x*
        A scalar numerical expression.

Return Value
------------

    The function :aimms:func:`MapVal` returns the (integer) mapping value of any real
    or special number *x*, according to the following table.

    .. table:: 

        =========== ========================================================================== ================
        **Value x** **Description**                                                            **MapVal value**
        *number*    any valid real number                                                      0
        ``UNDF``    undefined (result of an arithmetic error)                                  4
        ``NA``      not available                                                              5
        ``INF``     :math:`+\infty`                                                            6
        ``-INF``    :math:`-\infty`                                                            7
        ``ZERO``    numerically indistinguishable from zero, but has the logical value of one. 8
        =========== ========================================================================== ================


Example
-----------

.. code-block:: aimms

    _p_val := inf ;
    _p_return := mapval(_p_val); ! mapval(inf) returns 6.



.. seealso::

    Special numbers in AIMMS and the :aimms:func:`MapVal` function are discussed in
    full detail in :ref:`sec:expr.num.arith-ext` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
