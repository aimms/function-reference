.. aimms:procedure:: DataFileSetAcronym(datafile, acronym)

.. _DataFileSetAcronym:

DataFileSetAcronym
==================

The predefined set :aimms:set:`AllDataFiles` (and its subsets :aimms:set:`AllCases` and
:aimms:set:`AllDataSets`), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileSetAcronym` you can
set the acronym for the data file corresponding to any element of the
set :aimms:set:`AllDataFiles` (cases or datasets).

.. code-block:: aimms

    DataFileSetAcronym(
            datafile,     ! (input) element in the set AllDataFiles
            acronym       ! (input) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`.

    *acronym*
        A scalar string valued parameter. This parameter contains the acronym to
        be associated with the datafile. If an empty string is specified, any
        existing acronym will be deleted.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetAcronym`.
