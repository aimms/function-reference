.. warning::

   This article references outdated technology and is provided for historical purposes only. 
   It is not recommended to use this information as a primary source for current projects or documentation. 
   Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimmsxllibrary/index`  
   and the :doc:`dataexchange/index`.

.. aimms:procedure:: Spreadsheet::GetAllSheets(Workbook, Name)

.. _Spreadsheet::GetAllSheets:

Spreadsheet::GetAllSheets
=========================

The procedure :aimms:func:`Spreadsheet::GetAllSheets` obtains the names of all
sheets currently present in the specified Excel or OpenOffice Calc
workbook.

.. code-block:: aimms

    Spreadsheet::GetAllSheets(
            Workbook,       ! (input) scalar string expression
            SheetNames      ! (input) 1-dimensional string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Name*
        A 1-dimensional string parameter, which after successful execution will
        contain all present sheet names of the supplied workbook. The root set
        of the index should be a subset of Integers.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

