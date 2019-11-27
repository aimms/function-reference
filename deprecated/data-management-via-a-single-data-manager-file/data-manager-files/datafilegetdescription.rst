.. aimms:procedure:: DataFileGetDescription(datafile, name)

.. _DataFileGetDescription:

DataFileGetDescription
======================

The predefined set ``AllDataFiles`` (and its subsets ``AllCases`` and
``AllDataSets``), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileGetDescription` you
can obtain the description that the user entered via the properties of a
case or dataset.

.. code-block:: aimms

    DataFileGetDescription(
            datafile,      ! (input) element in the set AllDataFiles
            description    ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``.

    *name*
        A scalar string valued parameter. On return this parameter will contain
        the description of the datafile. If no description has been specified,
        then this string is empty.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetName`, :aimms:func:`DataFileGetAcronym`.
