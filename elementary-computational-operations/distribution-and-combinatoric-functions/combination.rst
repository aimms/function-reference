.. aimms:function:: Combination(n, m)

.. _Combination:

Combination
===========

The function :aimms:func:`Combination` computes the number of combinations of
length *m* in *n* items.

.. code-block:: aimms

    Combination(
               n,            ! (input) integer expression
               m             ! (input) integer expression
               )

Arguments
---------

    *n*
        An integer numerical expression :math:`\geq 0`.

    *m*
        An integer numerical expression in the range :math:`0,\dots,n`.

Return Value
------------

    The function :aimms:func:`Combination` returns :math:`\binom{n}{m}`, the number of
    combinations of length *m* in a given number of items *n*.

.. seealso::

    - Combinatoric functions are discussed in full detail in :ref:`table:expr.combinatoric`.
