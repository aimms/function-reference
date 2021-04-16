.. aimms:procedure:: Spreadsheet::RunMacro(Workbook, Name, MacroArgument01...MacroArgument30, Sheet)

.. _Spreadsheet::RunMacro:

Spreadsheet::RunMacro
=====================

.. warning::

  :doc:`index` are :doc:`deprecated <deprecation-table>`. One may use the :doc:`Articles/85/85-using-axll-library` or the :doc:`dataexchange/index`.

The procedure :aimms:func:`Spreadsheet::RunMacro` executes an Excel or OpenOffice
Calc macro.

.. code-block:: aimms

    Spreadsheet::RunMacro(
            Workbook,          ! (input) scalar string expression
            Name,              ! (input) scalar string expression
            [MacroArgument01], ! (optional) scalar expression
            ...
            [MacroArgument30], ! (optional) scalar expression
            [Sheet]            ! (optional) scalar string expression
            )

Arguments
---------

    *Workbook*
        A scalar string expression representing the Excel or Calc workbook. If
        this argument ends in ``.ods``, OpenOffice Calc is used. Otherwise,
        Excel is used.

    *Name*
        | The name of the macro to be executed. Please note that in the Excel
          case you need to specify the fully qualified name here. If, for
          example, you have a macro called ``ThisWorkbook.MyMacro``, only
          specifying ``MyMacro`` isn't sufficient. For the full name of an Excel
          macro, please refer to your Excel workbook and look under *Tools -
          Macro - Macros...*. Only in case you have created a so-called Visual
          Basic *Module* in your Excel workbook, you can just use the short name
          of your macro. Furthermore, it's also possible to call macro's which
          are located in a different workbook than the workbook it should be
          applied upon. In such cases, use the
          ``WorkbookContainingMacro!MacroName`` format for the name of the
          macro. Also, you have to make sure that the workbook containing the
          macro is opened before the call to RunMacro, since only macro's in
          opened workbooks can be found by Excel.
        | For OpenOffice Calc macros, you'll also need to specify the full path
          of a macro, for example ``"TheLibrary.TheModule.TheMacroToCall"``.
          Please note that Calc macros can be stored at either document scope,
          or at application scope. In the former case, the macros are stored
          within your document(i.e. ``.ods`` file), allowing you to distribute
          them easily to other users. In the latter case, the macros are stored
          in the Calc application on your machine, making it a bit harder to
          share your macros with other users, but enabling you to create macros
          that can be applied to all your workbooks.
        | By default, AIMMS assumes that the ``Name`` argument specifies a macro
          stored at document scope, since that is the more likely scenario for
          AIMMS use in combination with Calc. In case you want to call a macro
          at application scope, the ``Name`` argument should start with
          ``"Global."`` (case sensitive), for example
          ``"Global.TheLibrary.TheDocument.TheMacroToCall"``.
        | AIMMS does not support the calling of the OpenOffice standard macros
          (those are the macros under the ``OpenOffice.org Macros`` branch in
          the macro tree in OpenOffice).

    *MacroArgument01...MacroArgument30*
        A list of arguments to be passed to the macro. A maximum of 30 arguments
        is allowed. Only scalar arguments are supported. The scalar values can
        be of any type (numerical parameter, string parameter, element
        parameter, unit parameter, literal or variable). Furthermore, only input
        arguments are allowed.

    *Sheet*
        The sheet on which the macro should be applied. Please note: in a macro,
        it is possible to specify on which sheet certain actions should be
        performed. Clearly, in that case the Sheet argument does not influence
        this.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise. In case of an error
    the pre-defined AIMMS parameter :aimms:set:`CurrentErrorMessage` contains a description of what
    went wrong.

.. note::

    -  Element parameters that are passed as macro argument are usually
       passed to the workbook as strings, except when their range is a
       subset of integers.

    -  By calling the procedure :aimms:func:`Spreadsheet::SetActiveSheet` you can set the active sheet,
       after which the optional sheet argument can be omitted in procedures
       like this one.

    -  A call to this procedure with a specified sheet argument does not
       change the active sheet, except when the workbook does not have an
       active sheet yet.

    -  Upto AIMMS 3.11 this function was known as ``ExcelRunMacro``, which
       has become deprecated as of AIMMS 3.12.
