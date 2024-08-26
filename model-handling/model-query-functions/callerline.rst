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

Example
-------

The function :aimms:func:`CallerLine` is usually part of utility code, as follows:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 3

    Procedure pr_fragmentCallerLine {
        Body: {
            _p_callerLine := CallerLine(1);
            display _p_callerLine ;
        }
        Parameter _p_callerLine;
    }

Which can then be used as follows:

.. code-block:: aimms

    Procedure pr_testCallerLine {
        Body: {
            ! Hello
            
            pr_fragmentCallerLine();
        }
    }

A call to ``pr_testCallerLine`` produces in the listing file:

.. code-block:: aimms

    _p_callerLine := 3 ;

For a more extended illustration of how the function :aimms:func:`CallerLine` can be part of utility code, 
please check the example at :aimms:func:`CallerNumberOfLocations`.

References
-----------

    *  :aimms:func:`CallerAttribute`, 

    *  :aimms:func:`errh::Line`, 

    *  :aimms:func:`CallerNode`, and 

    *  :aimms:func:`CallerNumberOfLocations`.
