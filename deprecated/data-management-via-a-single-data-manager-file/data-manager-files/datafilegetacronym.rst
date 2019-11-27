.. aimms:procedure:: DataFileGetAcronym(datafile, acronym)

.. _DataFileGetAcronym:

DataFileGetAcronym
==================

The predefined set ``AllDataFiles`` (and its subsets ``AllCases`` and
``AllDataSets``), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileGetAcronym` you can
obtain the acronym that is specified in the data manager for any element
of the set ``AllDataFiles`` (cases or datasets).

.. code-block:: aimms

    DataFileGetAcronym(
            datafile,     ! (input) element in the set AllDataFiles
            acronym       ! (output) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``.

    *acronym*
        A scalar string valued parameter. On return this parameter will contain
        the acronym of the datafile. If no acronym is specified, then an empty
        string is returned.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetName`.
