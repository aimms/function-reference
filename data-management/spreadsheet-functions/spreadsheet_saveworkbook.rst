.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`Articles/85/85-using-axll-library` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::SaveWorkbook(Workbook, SaveAsName)

.. _Spreadsheet::SaveWorkbook:

Spreadsheet::SaveWorkbook
=========================

The procedure :aimms:func:`Spreadsheet::SaveWorkbook` saves the specified Excel or
OpenOffice Calc workbook. The workbook is saved with the name under
which it is known in AIMMS, unless the *SaveAsName* argument is
specified. Only when the *SaveAsName* argument is specified, or when
dealing with a workbook that has never been saved before (i.e. created
by a call to ``Spreadsheet::CreateWorkbook``), and a workbook with the
same name already exists on disk, the user is prompted with the question
whether or not to overwrite the existing file.

.. code-block:: aimms

    Spreadsheet::SaveWorkbook(
            Workbook,       ! (input) scalar string expression
            [SaveAsName]    ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *SaveAsName*
        The (new) name to be used for saving the workbook.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Upto AIMMS 3.11 this function was known as ``ExcelSaveWorkbook``,
       which has become deprecated as of AIMMS 3.12.
