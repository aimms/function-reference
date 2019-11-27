.. aimms:procedure:: SetAddRecursive(toSet, fromSet)

.. _SetAddRecursive:

SetAddRecursive
===============

With the procedure :aimms:procedure:`SetAddRecursive` you can merge the elements of one
set into another set.

.. code-block:: aimms

    SetAddRecursive(
         toSet,             ! (input/output) a set
         fromSet            ! (input) a set
         )

Arguments
---------

    *toSet*
        The set into which the elements of *fromSet* are merged.

    *fromSet*
        The set that you want to merge in *toSet*.

.. note::

    -  The sets *toSet* and *fromSet* should have the same root set.

    -  The difference between this function and a regular set assignment is
       that in case *fromSet* is not the domain of *toSet* all elements
       added to *toSet* will also be added to the domain set of *toSet*
