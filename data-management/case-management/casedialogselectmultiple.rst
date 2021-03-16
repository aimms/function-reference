.. aimms:procedure:: CaseDialogSelectMultiple(selectedCaseFiles)

.. _CaseDialogSelectMultiple:

CaseDialogSelectMultiple
========================

The procedure :aimms:func:`CaseDialogSelectMultiple` shows a case file selection
dialog box in which you can select multiple case files. The result is a
subset of :aimms:set:`AllCases` that can be used in multiple case views, or in
execution statements with the case dot notation.

.. code-block:: aimms

    CaseDialogSelectMultiple(
        selectedCaseFiles     ! (input/output) a subset of AllCases
        )

Arguments
---------

    *selectedCaseFiles*
        A subset of :aimms:set:`AllCases`. On entry, this subset is used to initalize the
        selection in the dialog box. On return, it contains the subset that has
        been selected by the user.

Return Value
------------

    The procedure returns 1 if the user selected a set of case files, and 0
    if the user cancelled the dialog box.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  This function returns 0 if the IDE is not loaded, for example when
       running the component version of AIMMS, or when running with the
       command line option ``--as-server``.

    -  You can use any subset of :aimms:set:`AllCases` as an argument to this
       function, but if you want to use it for a multiple case view in one
       of your pages, you should use the predefined set :aimms:set:`CurrentCaseSelection`.

    -  If the subset should have the selected cases in the order as
       specified in the dialog, you must make sure that the given subset has
       the attribute ``Order by`` set to ``user``.

.. seealso::

    The procedure :aimms:func:`CaseFileURLtoElement`, the string parameter :aimms:set:`CaseFileURL` and the set
    :aimms:set:`AllCases`.
