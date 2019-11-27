.. aimms:set:: ProfilerData

.. _ProfilerData:

ProfilerData
============

The predefined parameter :aimms:set:`ProfilerData` can be used by AIMMS to store
profiling information about the execution of procedures and the updating
of definitions.

.. code-block:: aimms

        Parameter ProfilerData {
            IndexDomain  :  ( IndexIdentifiers, IndexprofilerTypes );
        }

.. note::

    -  Profiling information is only stored in the parameter
       :aimms:set:`ProfilerData` if the profiler has been activated and if the option
       ``profiler_store_data`` has been set to ``On``.

    -  The number of reported hits is an postive integer and all reported
       profiling times are measured in seconds.

.. seealso::

    The function :aimms:func:`ProfilerStart` and the predefined identifier :aimms:set:`AllProfilerTypes`.
