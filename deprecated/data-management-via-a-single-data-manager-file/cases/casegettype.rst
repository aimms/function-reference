.. aimms:procedure:: CaseGetType(case, case\_type)

.. _CaseGetType:

CaseGetType
===========

The procedure :aimms:func:`CaseGetType` retrieves the case type for a specific
case.

.. code-block:: aimms

    CaseGetType(
            case,           ! (input) element of the set AllCases
            case_type       ! (output) element parameter into AllCaseTypes
            )

Arguments
---------

    *case*
        An element of the set :aimms:set:`AllCases`, refering to the case for which you
        want to retrieve its case type.

    *case\_type*
        An element parameter into :aimms:set:`AllCaseTypes`, on successfull return this
        argument will contain the case type for the given case.

Return Value
------------

    The procedure returns 1 on success, 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`CaseFileGetContentType`
       instead.
