.. aimms:function:: ProfilerCollectAllData(ProfilerData, GrossTimeThreshold, NetTimeThreshold)

.. _ProfilerCollectAllData:

ProfilerCollectAllData
======================

With the procedure :aimms:func:`ProfilerCollectAllData` you can retrieve the
current results of the profiler into a parameter in your model. This
procedure is especially usefull when you want to investigate timings of
a model that runs server-side, without the IDE. Data will be retrieved
for procedures and functions, and for parameter and sets that have a
definition.

.. code-block:: aimms

    ProfilerCollectAllData(
         ProfilerData,           ! (output) a 3-dimensional identifier
         GrossTimeThreshold,     ! (optional) scalar numerical parameter
         NetTimeThreshold        ! (optional) scalar numerical parameter
         )

Arguments
---------

    *ProfilerData*
        A three dimensional identifier where the indices represent (1) the
        identifiers, (2) the line numbers and (3) the specific profiler value.
        The first index should be an index in (a subset of) the predeclared set
        ``AllIdentifiers``, only for identifiers in this set the profiling data
        will be retrieved. The second index should be an index in a subset of
        ``Integers``. The third index should be an index in (a subset of) the
        predeclared set ``AllProfilerTypes``.

    *GrossTimeThreshold*
        An optional value, in seconds, which filters out all the profiler
        measurements where the gross time is smaller.

    *NetTimeThreshold*
        An optional value, in seconds, which filters out all the profiler
        measurements where the net time is smaller.

.. note::

    The procedure will only produce results when the profiler is currently
    active and some execution has already taken place. The subset of
    integers that is used for the line number will automatically be extended
    with all the line numbers that have actual measurements. So this set may
    be left empty when calling the procedure. For a procedure or function
    the timings of each individual statement is retrieved and stored using
    the corresponding line number. Besides that, the total timings of the
    procedure or function is stored as an entry with line number 0.

Example
-------

    With these declarations 

    .. code-block:: aimms

            Set Lines {
                Index: line;
                Subset of: Integers;
            }
            Parameter Results {
                IndexDomain: (IndexIdentifiers,line,IndexProfilerValues);
            }

    the procedure call 

    .. code-block:: aimms

            ProfilerCollectAllData(Results, GrossTimeThreshold: 0.5);

    fills
    the parameter ``Results`` with all profiler measurements for which the
    gross time is larger than 0.5 seconds.

.. seealso::

    The procedure :aimms:func:`ProfilerStart`.
