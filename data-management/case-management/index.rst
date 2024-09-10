Case Management
===============

If your project has set the option ``Data_Management_style`` to
``Disk_files_and_folders``, AIMMS supports a set of data management
functions, that allow you to modify the default data management
behavior.

There are two groups of functions. The *Core* functions and the GUI/IDE
related functions.

The core functions allow you to save data to and load data from case
files located on your system. These core functions do not keep track of
whether a specific case file is the current one, nor do they check
whether current data needs to be saved. These core functions are:

-  :aimms:func:`CaseFileLoad`
-  :aimms:func:`CaseFileMerge`
-  :aimms:func:`CaseFileSave`
-  :aimms:func:`CaseFileGetContentType`
-  :aimms:func:`CaseCompareIdentifier`
-  :aimms:func:`CaseCreateDifferenceFile`
-  :aimms:func:`CaseFileURLtoElement`
-  :aimms:func:`CaseFileSectionExists`
-  :aimms:func:`CaseFileSectionGetContentType`
-  :aimms:func:`CaseFileSectionLoad`
-  :aimms:func:`CaseFileSectionMerge`
-  :aimms:func:`CaseFileSectionRemove`
-  :aimms:func:`CaseFileSectionSave`

The GUI/IDE related data management functions can be used to create a
specific GUI for your own (modified) data management. They allow you to
re-use some of the default data management features. For example the
selecting of case files using dialog boxes, and the concept of a current
case.

-  :aimms:func:`CaseFileSetCurrent`
-  :aimms:func:`CaseCommandLoadAsActive`
-  :aimms:func:`CaseCommandLoadIntoActive`
-  :aimms:func:`CaseCommandMergeIntoActive`
-  :aimms:func:`CaseCommandNew`
-  :aimms:func:`CaseCommandSave`
-  :aimms:func:`CaseCommandSaveAs`
-  :aimms:func:`CaseDialogConfirmAndSave`
-  :aimms:func:`CaseDialogSelectForLoad`
-  :aimms:func:`CaseDialogSelectForSave`
-  :aimms:func:`CaseDialogSelectMultiple`
-  :aimms:func:`DataManagementExit`

.. toctree::
   :hidden:

   casefileload
   casecompareidentifier
   casefilemerge
   casefilesave
   casecreatedifferencefile
   casefilegetcontenttype
   casefilesectionexists
   casefilesectiongetcontenttype
   casefilesectionload
   casefilesectionmerge
   casefilesectionremove
   casefilesectionsave
   casecommandloadasactive
   casefilesetcurrent
   casefileurltoelement
   casecommandloadintoactive
   casecommandmergeintoactive
   casecommandnew
   casecommandsave
   casecommandsaveas
   casedialogconfirmandsave
   casedialogselectforload
   casedialogselectforsave
   casedialogselectmultiple
   datamanagementexit
