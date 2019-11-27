.. aimms:procedure:: DataManagerFileGetCurrent(filename)

.. _DataManagerFileGetCurrent:

DataManagerFileGetCurrent
=========================

With the procedure :aimms:func:`DataManagerFileGetCurrent` you can obtain the name
of the current data file.

.. code-block:: aimms

    DataManagerFileGetCurrent(
            filename          ! (output) a scalar string
            )

Arguments
---------

    *filename*
        A string to contain the name of the current data file (relative to the
        project directory).

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DataManagerFileNew`, :aimms:func:`DataManagerFileOpen`.
