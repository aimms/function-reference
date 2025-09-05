.. warning::

  This article references outdated technology and is provided for historical purposes only. 
  It is not recommended to use this information as a primary source for current projects or documentation. 
  Please refer to the latest documentation for up-to-date information, see more in: :doc:`aimms-libraries/repository-library/aimmsxllibrary/index` 
  and the :doc:`dataexchange/index`.

Spreadsheet Functions
---------------------

AIMMS supports the following functions for reading from and
writing to Excel and OpenOffice Calc workbooks:

.. toctree::
   :maxdepth: 1

   spreadsheet_columnname
   spreadsheet_columnnumber
   spreadsheet_setactivesheet
   spreadsheet_setvisibility
   spreadsheet_assignvalue
   spreadsheet_setoption
   spreadsheet_setupdatelinksbehavior
   spreadsheet_assignset
   spreadsheet_retrieveset
   spreadsheet_retrievevalue
   spreadsheet_assignparameter
   spreadsheet_retrieveparameter
   spreadsheet_assigntable
   spreadsheet_clearrange
   spreadsheet_retrievetable
   spreadsheet_addnewsheet
   spreadsheet_copyrange
   spreadsheet_deletesheet
   spreadsheet_getallsheets
   spreadsheet_runmacro
   spreadsheet_closeworkbook
   spreadsheet_createworkbook
   spreadsheet_saveworkbook
   spreadsheet_print

.. note::
  
  The functions operate on OpenOffice Calc workbooks, if the ``WorkbookName`` argument ends in ``.ods``. 
  In all other cases, the functions operate on Excel workbooks.