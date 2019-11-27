.. aimms:set:: AllProfilerTypes

.. _AllProfilerTypes:

AllProfilerTypes
================

The predefined set :aimms:set:`AllProfilerTypes` contains the names of all types
of profiler data that can be stored in the predefined identifier
``ProfilerData``.

.. code-block:: aimms

        Set AllProfilerTypes {
            Index      :  IndexprofilerTypes;
        }

Definition
----------

    The set :aimms:set:`AllProfilerTypes` currently contains the profiler types
    '*hits*', '*gross time*', and '\ *net time*\ '.

.. seealso::

    The function :aimms:func:`ProfilerStart` and the predefined parameter :aimms:set:`ProfilerData`.
