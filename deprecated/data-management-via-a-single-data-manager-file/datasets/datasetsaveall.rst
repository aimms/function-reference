.. aimms:procedure:: DatasetSaveAll([confirm])

.. _DatasetSaveAll:

DatasetSaveAll
==============

The procedure :aimms:func:`DatasetSaveAll` saves the data of all data category to
the active datasets. If there are no named active datasets, then the
procedure behaves according to the ``DatasetSaveAs`` procedure.

.. code-block:: aimms

    DatasetSaveAll(
            [confirm]      ! (optional) 0, 1 or 2
            )

Arguments
---------

    *confirm (optional)*
        An integer to indicate whether or not the procedure should ask for
        confirmation before overwriting the existing datasets. If 0, then no
        confirmation dialog box is shown. If 1 (default), then whether or not
        the confirmation dialog box is shown depends on the case type
        properties. If 2, then always a confirmation dialog box is shown.

Return Value
------------

    The procedure returns 1 if the datasets are saved successfully. It
    returns 0 if the user canceled the save operation. If any other error
    occurs, then the procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain
    an error message.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

.. seealso::

    The procedures :aimms:func:`DatasetSaveAs`, :aimms:func:`DatasetSave`, :aimms:func:`DatasetLoadCurrent`, :aimms:func:`DatasetGetChangedStatus`.
