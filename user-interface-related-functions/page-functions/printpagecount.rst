.. aimms:procedure:: PrintPageCount(page)

.. _PrintPageCount:

PrintPageCount
==============

The procedure :aimms:func:`PrintPageCount` will return how many sheets of paper
are needed to print a single print page in the interface.

.. code-block:: aimms

    PrintPageCount(
            page            ! (input) scalar string expression
            )

Arguments
---------

    *page*
        A string expression representing the name of the page that you want to
        print. This name is the unique name as it appears in the Page Manager
        tree.

Return Value
------------

    The procedure returns the number of sheets needed, or 0 if the page
    cannot be printed.

.. seealso::

    The procedure :aimms:func:`PrintPage`.
