.. aimms:procedure:: DataFileSetComment(datafile, comment)

.. _DataFileSetComment:

DataFileSetComment
==================

The predefined set ``AllDataFiles`` (and its subsets ``AllCases`` and
``AllDataSets``), is an integer set. The mapping of these integers onto
the cases and datasets in the project is maintained by the data manager,
and is not editable. With the procedure :aimms:func:`DataFileSetComment` you can
set the comment for the data file corresponding to any element of the
set ``AllDataFiles`` (cases or datasets).

.. code-block:: aimms

    DataFileSetComment(
            datafile,     ! (input) element in the set AllDataFiles
            comment       ! (input) scalar string parameter
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``.

    *comment*
        A scalar string valued parameter. This parameter contains the comment to
        be associated with the datafile. If an empty string is specified, any
        existing comment will be deleted.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataFileExists`, :aimms:func:`DataFileGetComment`.
