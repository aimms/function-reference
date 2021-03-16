.. aimms:procedure:: DataFileCopy(datafile, acronym, copiedDatafile)

.. _DataFileCopy:

DataFileCopy
============

With the procedure :aimms:func:`DataFileCopy` you can copy a data file stored
within a data manager file, to another data file within the same data
manager file.

.. code-block:: aimms

    DataFileCopy(
            datafile,      ! (input) element in the set AllDataFiles
            acronym,       ! (input) string
            copiedDatafile ! (output) element parameter into AllDataFiles
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`, :aimms:set:`AllCases` or :aimms:set:`AllDataSets`.

    *acronym*
        The name of the new data file to be created

    *copiedDatafile*
        On success, contains the element in :aimms:set:`AllDataFiles` associated with the
        datafile into which the original data file was copied.

Return Value
------------

    The procedure returns 1 if the data file has been copied, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If a datafile with the given acronym already exists in the data
       manager file, the call to :aimms:func:`DataFileCopy` will fail.
