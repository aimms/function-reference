.. aimms:function:: Permutation(n, m)

.. _Permutation:

Permutation
===========

The function :aimms:func:`Permutation` computes the number of permutations of
length :math:`m` in :math:`n` items.

.. code-block:: aimms

    Permutation(
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

    The function :aimms:func:`Permutation` returns :math:`m!\cdot{\binom{n}{m}}`, the
    number of permutations of length *m* in a given number of items *n*.

.. seealso::

    Combinatoric functions are discussed in full detail in :ref:`table:expr.combinatoric`.
