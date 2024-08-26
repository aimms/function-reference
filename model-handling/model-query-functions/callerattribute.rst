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
        the range :math:`\{ 1 \ldots` :aimms:func:`CallerNumberOfLocations` :math:`\}`. The value 1, refers to the
        caller of the currently running procedure.

Return Value
------------

    This function returns an element in :aimms:set:`AllAttributeNames`.


Example
-------

The function :aimms:func:`CallerAttribute` is usually part of utility code, as follows:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 3

    Procedure pr_fragmentCallerAttribute {
        Body: {
            _ep_callerAttribute := CallerAttribute(1);
            display _ep_callerAttribute ;
        }
        ElementParameter _ep_callerAttribute {
            Range: AllAttributeNames;
        }
    }

Which can then be used as follows:

.. code-block:: aimms

    Procedure pr_testCallerAttribute {
        Body: {
            pr_fragmentCallerAttribute();
        }
    }

A call to ``pr_testCallerAttribute`` produces in the listing file:

.. code-block:: aimms

    _ep_callerAttribute := 'body' ;

For a more extended illustration of how the function :aimms:func:`CallerAttribute` can be part of utility code, 
please check the example at :aimms:func:`CallerNumberOfLocations`.

References
-----------

    *  :aimms:func:`errh::Attribute`, 

    *  :aimms:func:`CallerLine`, 

    *  :aimms:func:`CallerNode`, and 

    *  :aimms:func:`CallerNumberOfLocations`.
