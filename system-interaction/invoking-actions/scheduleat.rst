.. aimms:procedure:: ScheduleAt(starttime, procedure)

.. _ScheduleAt:

ScheduleAt
==========

With the procedure :aimms:func:`ScheduleAt` you schedule a specific procedure to
be run at a specified moment in time.

.. code-block:: aimms

    ScheduleAt(
         starttime,         ! (input) scalar string expression
         procedure          ! (input) element of the set AllProcedures
         )

Arguments
---------

    *starttime*
        A string representing the time at which you want to start the execution
        of the specified procedure. This time must be respresent using AIMMS'
        standard time format: "YYYY-MM-DD hh:mm:ss".

    *procedure*
        An element in the set :aimms:set:`AllProcedures`. This procedure cannot have any
        arguments.

Return Value
------------

    The procedure returns 1 on success, and 0 if AIMMS could not schedule
    the procedure at the specified start time. On failure, the pre-defined
    identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. note::

    If at the specified start time AIMMS is busy running some other task,
    then the procedure will start as soon as AIMMS has finished this task.
    If you want to run a procedure at regular intervals, then you can
    re-schedule the procedure from within the scheduled procedure itself.
