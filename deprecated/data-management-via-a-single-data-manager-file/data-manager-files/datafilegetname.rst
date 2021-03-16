.. aimms:procedure:: DataFileGetName(datafile, name)

.. _DataFileGetName:

DataFileGetName
===============

The predefined set :aimms:set:`AllDataFiles` (and its subsets :aimms:set:`AllCases` and
:aimms:set:`AllDataSets`), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileGetName` you can
obtain the name in the data manager for any element of the set
:aimms:set:`AllDataFiles` (cases or datasets).

.. code-block:: aimms

    DataFileGetName(
            datafile,     ! (input) element in the set AllDataFiles
            name          ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set :aimms:set:`AllDataFiles`.

    *name*
        A scalar string valued parameter. On return this parameter will contain
        the name of the datafile. This name does not include the name of the
        folder(s) in which it is located.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetPath`, :aimms:func:`DataFileGetAcronym`.
