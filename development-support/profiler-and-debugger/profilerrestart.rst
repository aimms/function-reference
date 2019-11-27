.. aimms:function:: ProfilerRestart()

.. _ProfilerRestart:

ProfilerRestart
===============

The procedure :aimms:func:`ProfilerRestart` clears the execution time measurement
data of all statements and definitions.

.. code-block:: aimms

    ProfilerRestart 

.. note::

    -  This procedure is the programmatic counterpart of the **Profiler** -
       **Restart** menu command.

    -  This procedure only has effect when the profiler has been activated.

.. seealso::

    The procedure :aimms:func:`ProfilerContinue` and :aimms:func:`ProfilerPause`.
