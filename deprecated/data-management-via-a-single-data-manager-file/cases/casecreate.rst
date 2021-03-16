.. aimms:procedure:: CaseCreate(case\_path, case)

.. _CaseCreate:

CaseCreate
==========

The procedure :aimms:func:`CaseCreate` creates a new case node in the Data
Management tree. The name of the case and the folder in which it is
created is given as an argument to the function.

.. code-block:: aimms

    CaseCreate(
              case_path,    ! (input) scalar string expression
              case          ! (output) element parameter into AllCases
              )

Arguments
---------

    *case\_path*
        A string expression holding the path and name of the new case. The path
        is specified relative to the root of the case tree.

    *case*
        An element parameter into :aimms:set:`AllCases`. On successful return this parameter
        will refer to the newly created element in :aimms:set:`AllCases`.

Return Value
------------

    The procedure returns 1 if the case is created successfully. It returns
    0 if the case could not be created or if the case already exists.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the specified path contains folders that do not exist, then these
       folders are created automatically. To check whether a specific case
       path already exists you can use the function ``CaseFind``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders`` there is no valid replacement.

.. seealso::

    The procedures :aimms:func:`CaseFind`, :aimms:func:`CaseDelete`.
