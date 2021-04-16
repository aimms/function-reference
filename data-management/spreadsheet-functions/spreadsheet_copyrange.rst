.. aimms:procedure:: Spreadsheet::CopyRange(Workbook, SourceRange, DestinationRange, SourceSheet, DestinationSheet)

.. _Spreadsheet::CopyRange:

Spreadsheet::CopyRange
======================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::CopyRange` copies the contents of a
complete Excel or OpenOffice Calc range to another Excel/Calc range.

.. code-block:: aimms

    Spreadsheet::CopyRange(
            Workbook,          ! (input) scalar string expression
            SourceRange,       ! (input) scalar string expression
            DestinationRange,  ! (input) scalar string expression
            [SourceSheet],     ! (optional) scalar string expression
            [DestinationSheet] ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *SourceRange*
        A scalar string expression containing a reference to the range in the
        spreadsheet that should be copied from.

    *DestinationRange*
        A scalar string expression containing a reference to the range in the
        spreadsheet that should be copied to.

    *SourceSheet*
        The sheet containing the *SourceRange*. Default is the active sheet. If
        the source range is a uniquely named range, no active sheet needs to be
        set, since named ranges already contain a reference to a sheet.

    *DestinationSheet*
        The sheet containing the *DestinationRange*. Default is the active
        sheet. If the destination range is a uniquely named range, no active
        sheet needs to be set, since named ranges already contain a reference to
        a sheet.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  By calling the procedure :aimms:func:`Spreadsheet::SetActiveSheet` you can set the active sheet,
       after which the optional sheet arguments can be omitted in this
       procedure. The active sheet will then be used both for the source and
       the destination sheet of :aimms:func:`Spreadsheet::CopyRange`.

    -  In case that the active sheet was not set before the call to this
       function, the active sheet is set to the *SourceSheet* argument, if
       supplied. If the *SourceSheet* argument is not supplied, the active
       sheet is set to the *DestinationSheet* argument, if supplied.
       Otherwise, the active sheet is not changed.

    -  Upto AIMMS 3.11 this function was known as ``ExcelCopyRange``, which
       has become deprecated as of AIMMS 3.12.
