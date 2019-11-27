.. aimms:function:: ProfilerStart()

.. _ProfilerStart:

ProfilerStart
=============

The procedure :aimms:func:`ProfilerStart` starts measuring the execution time of
statements and definitions.

.. code-block:: aimms

    ProfilerStart 

.. note::

    When the option ``profiler_store_data`` has been set to ``On`` profiling
    information is stored in the predefined identifier ``ProfilerData``.

.. seealso::

    The procedures :aimms:func:`ProfilerPause`, :aimms:func:`ProfilerContinue` and :aimms:func:`ProfilerRestart` and the predefined
    identifier :aimms:set:`ProfilerData`.
