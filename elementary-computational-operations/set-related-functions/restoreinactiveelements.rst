.. aimms:procedure:: RestoreInactiveElements(SearchSet, SearchIdentifiers, UsedElements)

.. _RestoreInactiveElements:

RestoreInactiveElements
=======================

The procedure :aimms:procedure:`RestoreInactiveElements` finds and restores all
elements that were previously removed from a particular set, but for
which inactive data still exists in a given collection of indexed model
identifiers.

.. code-block:: aimms

    RestoreInactiveElements(
         SearchSet,          ! (input/output) a set
         SearchIdentifiers,  ! (input) a subset of AllIdentifiers
         UsedElements        ! (output) a subset
         )

Arguments
---------

    *SearchSet*
        The set for which you want to find the inactive elements.

    *SearchIdentifiers*
        A subset of :aimms:set:`AllIdentifiers`, holding identifiers that are indexed over
        *SearchSet*.

    *UsedElements*
        A subset of *SearchSet*. On return this subset will contain all the
        inactive elements that are currently used (i.e. have corresponding
        nondefault values) in the identifiers contained in *SearchIdentifiers*.

.. note::

    The inactive elements found are placed in the *result-set*, but are also
    automatically added to the *search-set*.
