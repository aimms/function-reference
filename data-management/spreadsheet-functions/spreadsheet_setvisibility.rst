.. warning::

    This article references outdated technology and is provided for historical purposes only. 
    It is not recommended to use this information as a primary source for current projects or documentation. 
    Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimmsxllibrary/index` 
    and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::SetVisibility(Workbook, Visibility)

.. _Spreadsheet::SetVisibility:

Spreadsheet::SetVisibility
==========================

The procedure :aimms:func:`Spreadsheet::SetVisibility` turns the visibility mode
of the given Excel or OpenOffice Calc workbook on or off.

.. code-block:: aimms

    Spreadsheet::SetVisibility(
            Workbook,       ! (input) scalar string expression
            Visibility      ! (input) scalar element expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Visibility*
        A scalar element expression in the pre-defined AIMMS set :aimms:set:`OnOff`
        specifying whether to show or hide the specified workbook.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  If the workbook is not yet open, it will be opened.

    -  Upto AIMMS 3.11 this function was known as ``ExcelSetVisibility``,
       which has become deprecated as of AIMMS 3.12.
