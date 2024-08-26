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



Example
-------

The function :aimms:func:`CallerNode` is usually part of utility code, as follows:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 3

    Procedure pr_fragmentCallerNode {
        Body: {
            _ep_callerNode := CallerNode(1);
            display _ep_callerNode ;
        }
        ElementParameter _ep_callerNode {
            Range: AllSymbols;
        }
    }

Which can then be used as follows:

.. code-block:: aimms

    Procedure pr_testCallerNode {
        Body: {
            ! Hello
            
            pr_fragmentCallerNode();
        }
        aimmsunit::TestSuite: modelQuery;
    }

A call to ``pr_testCallerNode`` produces in the listing file:

.. code-block:: aimms

    _ep_callerNode := 'chapterModel::sectionModelQuery::funcCallerNode::pr_testCallerNode' ;


For a more extended illustration of how the function :aimms:func:`CallerNode` can be part of utility code, 
please check the example at :aimms:func:`CallerNumberOfLocations`.

References
-----------

    *  :aimms:func:`CallerAttribute`, 

    *  :aimms:func:`CallerLine`, 

    *  :aimms:func:`errh::Node`, and 

    *  :aimms:func:`CallerNumberOfLocations`.
