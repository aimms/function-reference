.. aimms:procedure:: DataManagerExport(filename, datafiles)

.. _DataManagerExport:

DataManagerExport
=================

With the procedure :aimms:func:`DataManagerExport` you can export a collection of
cases and datasets from the data management tree to a new data file.

.. code-block:: aimms

    DataManagerExport(
            filename,       ! (input) a scalar string expression
            datafiles       ! (input/output) a subset of AllDataFiles
            )

Arguments
---------

    *filename*
        A string containing the name of the data file to which the cases and
        datasets must be exported.

    *datafiles*
        A subset of ``AllDataFiles``, containing the cases and datasets that you
        want to export. Any dataset that is referred to by a case in this set is
        automatically added to the set.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedure :aimms:func:`DataManagerImport`.
