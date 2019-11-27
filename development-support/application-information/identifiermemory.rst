.. aimms:function:: IdentifierMemory(Identifier, IncludePermutations)

.. _IdentifierMemory:

IdentifierMemory
================

With the function :aimms:func:`IdentifierMemory` you can determine the total
amount of memory occupied by the identifier.

.. code-block:: aimms

    IdentifierMemory(
         Identifier,         ! (input) scalar element parameter
         IncludePermutations ! (optional, default 1) scalar binary expression
         )

Arguments
---------

    *Identifier*
        An element expression in the set :aimms:set:`AllIdentifiers` specifying the identifier for
        which the amount of occupied memory should be determined.

    *IncludePermutations*
        An 0-1 value indicating whether the amount of memory occupied by
        permutations of the identifier should also be included in the total
        memory determination.

Return Value
------------

    The function reports the sum of the memory occupied by the identifier,
    its suffixes and the associated hidden identifiers (that are introduced
    as temporary identifiers by the AIMMS compiler/execution engine. The
    unit of measurement for this function is bytes.

.. note::

    The return value of this function differs from the value reported in the
    'Memory Usage' column of the **Identifier Cardinalities** dialog box
    because in the **Identifier Cardinalities** dialog box the value for
    hidden identifiers and suffixes are reported separately.
