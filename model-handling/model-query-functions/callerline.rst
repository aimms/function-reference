.. aimms:function:: CallerLine(Depth)

.. _CallerLine:

CallerLine
==========

The function :aimms:func:`CallerLine` returns the line of a node that is on the
current execution stack.

.. code-block:: aimms

    CallerLine(
         Depth       ! (optional) scalar element parameter
         )

Arguments
---------

    *Depth*
        An numeric optional expression with default 1. The value should be in
        the range :math:`\{ 1 \ldots` :aimms:func:`CallerNumberOfLocations` :math:`\}`. The value 1, refers to the
        caller of the currently running procedure.

Return Value
------------

    This function returns a line number.

.. seealso::

    -  The example at :aimms:func:`CallerNumberOfLocations`

    -  The functions :aimms:func:`CallerAttribute`, :aimms:func:`errh::Line`, :aimms:func:`CallerNode`, and :aimms:func:`CallerNumberOfLocations`.
