.. aimms:function:: DebuggerBreakPoint(only\_if\_active)

.. _DebuggerBreakPoint:

DebuggerBreakPoint
==================

The procedure :aimms:func:`DebuggerBreakPoint` breaks execution and activates the
debugger when needed.

.. code-block:: aimms

    DebuggerBreakPoint(
         [only_if_active]       ! (optional, default 0) scalar binary expression
         )

Arguments
---------

    *only\_if\_active*
        When this argument equals 1, execution is only stopped when the debugger
        is active. If this argument equals 0 the execution is always stopped and
        the debugger is activated if necessary.

.. note::

    -  The debugger and profiler are exclusive. When the profiler is active,
       this procedure has no effect.

    -  This procedure has no effect in end-user mode because the debugger is
       not available in end-user mode.
