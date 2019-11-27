.. aimms:procedure:: PrintEndReport(None)

.. _PrintEndReport:

PrintEndReport
==============

With the procedure ``PageEndReport`` you finish the printing of a report
that was started via a call to ``PrintStartReport``.

.. code-block:: aimms

    PrintEndReport

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 on success, or 0, if there was no current
    report.

.. seealso::

    The procedures :aimms:func:`PrintStartReport`, :aimms:func:`PrintPage`.
