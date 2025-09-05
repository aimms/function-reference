.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`Articles/85/85-using-axll-library` 
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::RetrieveSet(Workbook, Set, Range, Sheet, Mode)

.. _Spreadsheet::RetrieveSet:

Spreadsheet::RetrieveSet
========================

The procedure :aimms:func:`Spreadsheet::RetrieveSet` fills an AIMMS set based on
the data in the given range of an Excel or OpenOffice Calc workbook.

.. code-block:: aimms

    Spreadsheet::RetrieveSet(
            Workbook,       ! (input) scalar string expression
            Set,            ! (output) set identifier
            Range,          ! (input) scalar string expression
            [Sheet],        ! (optional) scalar string expression
            [Mode]          ! (optional) scalar element expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is

    *Set*
        The set to be filled.

    *Range*
        The range in the workbook based on which the *Set* must be filled.

    *Sheet*
        The sheet from which the data should be read. Default is the active
        sheet.

    *Mode*
        Element in the pre-defined set :aimms:set:`MergeReplace`. In *replace* mode, the AIMMS
        set is emptied before being filled. In *merge* mode, the new elements
        are added to the existing set. By default, the set is filled in replace
        mode.

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

    -  Upto AIMMS 3.11 this function was known as ``ExcelRetrieveSet``,
       which has become deprecated as of AIMMS 3.12.
