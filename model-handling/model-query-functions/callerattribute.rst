.. aimms:function:: CallerAttribute(Depth)

.. _CallerAttribute:

CallerAttribute
===============

The function :aimms:func:`CallerAttribute` returns the attribute of a node that is
on the current execution stack.

.. code-block:: aimms

    CallerAttribute(
                   Depth      ! (optional) scalar element parameter
                   )

Arguments
---------

    *Depth*
        An numeric optional expression with default 1. The value should be in
        the range :math:`\{ 1 \ldots ` :aimms:func:`CallerNumberOfLocations` :math:`\}` The value 1, refers to the
        caller of the currently running procedure.

Return Value
------------

    This function returns an element in :aimms:set:`AllAttributeNames`.

.. seealso::

    -  The example at :aimms:func:`CallerNumberOfLocations`.

    -  The functions :aimms:func:`errh::Attribute`, :aimms:func:`CallerLine`, :aimms:func:`CallerNode`, and :aimms:func:`CallerNumberOfLocations`.
