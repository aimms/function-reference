.. aimms:procedure:: FindUsedElements(SearchSet, SearchIdentifiers, UsedElements)

.. _FindUsedElements:

FindUsedElements
================

The procedure :aimms:procedure:`FindUsedElements` finds all elements of a particular
set that are in use in a given collection of indexed model identifiers.

.. code-block:: aimms

    FindUsedElements(
         SearchSet,           ! (input) a set
         SearchIdentifiers,   ! (input) a subset of AllIdentifiers
         UsedElements         ! (output) a subset
         )

Arguments
---------

    *SearchSet*
        The set for which you want to find the used elements.

    *SearchIdentifiers*
        A subset of :aimms:set:`AllIdentifiers`, holding identifiers that are indexed over
        ``SearchSet``.

    *UsedElements*
        A subset of *SearchSet*. On return this subset will contain the elements
        that are currently used (i.e. have corresponding nondefault values) in
        the identifiers contained in *SearchIdentifiers*.
