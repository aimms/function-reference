.. aimms:procedure:: DataFileGetTime(datafile, time)

.. _DataFileGetTime:

DataFileGetTime
===============

With the procedure :aimms:func:`DataFileGetTime` you can obtain the time on which
the data of a specific case or dataset was last modified (saved).

.. code-block:: aimms

    DataFileGetTime(
            datafile,      ! (input) element in the set AllDataFiles
            time           ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`.

    *time*
        A scalar string valued parameter. On return this parameter will contain
        a string representation of the modification time, using AIMMS' standard
        date and time format: "YYYY-MM-DD hh:mm:ss".

Return Value
------------

    The procedure returns 1 if the given datafile exists and contains saved
    data. If the datafile does not exist, or if no data has yet been saved
    in the datafile, then the procedure returns 0.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`FileTime`.
