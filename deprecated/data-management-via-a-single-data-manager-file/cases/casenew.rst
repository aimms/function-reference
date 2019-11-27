.. aimms:procedure:: CaseNew(None)

.. _CaseNew:

CaseNew
=======

The procedure :aimms:func:`CaseNew` starts a new case. The procedure is similar to
the command **New Case** from the **Data** menu. The procedure does not
change any of the current data, it only assures that there is no longer
a current case. If you did have a current case and the data of this case
has been changed, then AIMMS will ask whether or not this case should be
saved first.

.. code-block:: aimms

    CaseNew

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 on success. If the user cancelled the operation,
    then the procedure returns 0. If any other error occurs then the
    procedure returns :math:`-1` and :aimms:set:`CurrentErrorMessage` will contain a proper error
    message.

.. note::

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseCommandNew`
       instead.

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If you use :aimms:func:`CaseNew`, then the name of this new case is not
       specified until you save the case. If you want to start a new named
       case, then you can use the following piece of code:

    .. code-block:: aimms

               if ( CaseGetChangedStatus ) then
                   if ( CaseSave = 0 ) then
                       return ;
                   endif ;
               endif ;
               if ( CaseSelectNew( a_case ) ) then
                   CaseSetCurrent( a_case );
                   CaseSetChangedStatus( a_case, 1 );
               endif ;

.. seealso::

    The procedures :aimms:func:`CaseLoadCurrent`, :aimms:func:`CaseSave`, :aimms:func:`CaseSelectNew`, :aimms:func:`CaseSetCurrent`.
