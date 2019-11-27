.. aimms:procedure:: DataManagerFileOpen(filename, UseAsDefault)

.. _DataManagerFileOpen:

DataManagerFileOpen
===================

With the procedure :aimms:func:`DataManagerFileOpen` you can open an existing data
file. On success, the data file will be used as the current data file
for the project.

.. code-block:: aimms

    DataManagerFileOpen(
            filename,         ! (input) a scalar string expression
            [UseAsDefault]    ! (optional, default 1) a scalar binary expression
            )

Arguments
---------

    *filename*
        A string containing the name of the existing data file (relative to the
        project directory).

    *UseAsDefault*
        A binary value to indicate whether the data file should be used as the
        default data file the next time the project is opened (value 1) or not
        (value 0).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataManagerFileNew`, :aimms:func:`DataManagerFileGetCurrent`.
