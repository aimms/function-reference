.. aimms:function:: CallerNode(Depth)

.. _CallerNode:

CallerNode
==========

The function :aimms:func:`CallerNode` returns the node that is on the current
execution stack.

.. code-block:: aimms

    CallerNode(
         Depth      ! (optional) scalar element parameter
         )

Arguments
---------

    *Depth*
        An numeric optional expression with default 1. The value should be in
        the range :math:`\{ 1 \ldots` :aimms:func:`CallerNumberOfLocations` :math:`\}`. The value 1, refers to the
        caller of the currently running procedure.

Return Value
------------

    This function returns an element in :aimms:set:`AllSymbols`.

.. seealso::

    -  The example at :aimms:func:`CallerNumberOfLocations`

    -  The functions :aimms:func:`CallerAttribute`, :aimms:func:`CallerLine`, :aimms:func:`errh::Node`, and :aimms:func:`CallerNumberOfLocations`.
