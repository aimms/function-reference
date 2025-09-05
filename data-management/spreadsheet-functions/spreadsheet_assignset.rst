.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimms-libraries/repository-library/aimmsxllibrary/index` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::AssignSet(Workbook, Set, Range, Sheet)

.. _Spreadsheet::AssignSet:

Spreadsheet::AssignSet
======================

The procedure :aimms:func:`Spreadsheet::AssignSet` writes the elements of an AIMMS
set into the given range of an Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::AssignSet(
            Workbook,       ! (input) scalar string expression
            Set,            ! (input) set identifier
            Range,          ! (input) scalar string expression
            [Sheet]         ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Set*
        The AIMMS set to be written to the spreadsheet.

    *Range*
        A scalar string expression containing the range in the sheet to which
        the *Set* should be written.

    *Sheet*
        The sheet to which the *Set* should be written. Default is the active
        sheet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  By calling the procedure :aimms:func:`Spreadsheet::SetActiveSheet` you can set the active sheet,
       after which the optional sheet argument can be omitted in procedures
       like this one.

    -  A call to this procedure with a specified sheet argument does not
       change the active sheet, except when the workbook does not have an
       active sheet yet.

    -  Upto AIMMS 3.11 this function was known as ``ExcelAssignSet``, which
       has become deprecated as of AIMMS 3.12.
