.. aimms:procedure:: Spreadsheet::SetUpdateLinksBehavior(UpdateLinksBehavior)

.. _Spreadsheet::SetUpdateLinksBehavior:

Spreadsheet::SetUpdateLinksBehavior
===================================

This procedure specifies how Excel or OpenOffice Calc workbooks
containing links to other workbooks should be opened. In the Excel case,
such links can be either links to external workbooks or to remote
workbooks. In the Calc case, this distinction is not made. If you do not
call this procedure before using an Excel workbook containing links, you
are prompted whether you want the links to be updated or not. In the
OpenOffice case, you will get the default behavior as specified in the
update setting\ :math:`^*`, if no Calc dialogs are required. This
procedure is designed to give the AIMMS user control over the Excel and
Calc behavior regarding links.

.. code-block:: aimms

    ExcelSetUpdateLinksBehavior(
            UpdateLinksBehavior  ! (input) scalar integer expression
            )

Arguments
---------

    *UpdateLinksBehavior*
        A scalar expression that sets the behavior of Excel or Calc when a
        workbook is opened. Possible values are:

        -  0: (Excel) Excel prompts the user (the Excel default behavior).

        -  1: (Excel) Do not update any links.

        -  2: (Excel) Only update external links.

        -  3: (Excel) Only update remote links

        -  4: (Excel) Update both external and remote links

        -  5: (Calc) Do not update any links.

        -  6: (Calc) If the update setting in Calc\ :math:`^*` is 'Always', all
           links are updated. Otherwise, no links are updated (the Calc default
           behavior).

        -  7: (Calc) Always update the links.

        Argument values 0 to 4 are for Excel workbooks, values 5 to 7 are for
        OpenOffice Calc workbooks. :math:`^*` This setting is called *Update
        links when opening* and can be found in the Calc menu, under Tools -
        Options - OpenOffice.org Calc - General.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  When the procedure is called, the setting remains valid for all
       consequent workbooks that will be opened, until the procedure is
       called again with a different setting.

    -  In case you use both Excel and Calc workbooks with links in your
       AIMMS application, you should call this function twice: once with an
       argument to control the Excel behavior, and once with an argument to
       control the Calc behavior. The setting of the first call will be
       remembered when you do the second call. For example: first call
       ``Spreadsheet::SetUpdateLinksBehavior(1)``, to specify that Excel
       workbooks should not update their links, and then call
       ``Spreadsheet::SetUpdateLinksBehavior(7)``, to specify that Calc
       workbooks should always update their links upon opening.

    -  Upto AIMMS 3.11 this function was known as
       ``ExcelSetUpdateLinksBehavior``, which has become deprecated as of
       AIMMS 3.12.
