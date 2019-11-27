.. aimms:function:: ActiveCard(Identifier, Suffix)

.. _ActiveCard:

ActiveCard
==========

The function :aimms:func:`ActiveCard` returns the cardinality of active elements
in its identifier argument, or the cardinality of active elements of a
suffix of that identifier.

.. code-block:: aimms

    ActiveCard(
        Identifier,    ! (input) identifier reference
        [Suffix]       ! (optional) element in the set AllSuffixNames
        )

Arguments
---------

    *Identifier*
        A reference to a set or an indexed identifier.

    *Suffix*
        An element in the predefined set :aimms:set:`AllSuffixNames`.

Return Value
------------

    If *Identifier* is a set, the function ActiveCard returns the number of
    active elements in *Identifier*. If *Identifier* is an indexed
    identifier, the function ActiveCard returns the number of nondefault
    values stored for *Identifier*. If *Suffix* is given, the number of
    nondefault values stored for the given suffix of *Identifier*.

.. note::

    The :aimms:func:`ActiveCard` function cannot be applied to slices of indexed
    identifiers. In such a case, you can use the ``Count`` operator to count
    the number of nondefault elements.

.. seealso::

    The function :aimms:func:`Card` and ``Count`` operator (see also Section 6.1.6 of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__).
