.. aimms:procedure:: CaseFind(case\_path, case)

.. _CaseFind:

CaseFind
========

The procedure :aimms:func:`CaseFind` searches the Data Management tree for a case
with a specific name.

.. code-block:: aimms

    CaseFind(
            case_path,    ! (input) scalar string expression
            case          ! (output) element parameter into AllCases
            )

Arguments
---------

    *case\_path*
        A string expression holding the path and name of a case. The path is
        specified relative to the root of the case tree.

    *case*
        An element parameter into :aimms:set:`AllCases`. On successfull return this
        parameter will refer to the case found.

Return Value
------------

    The procedure returns 1 if the case is found, and 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders`` there is no valid replacement.

.. seealso::

    The procedures :aimms:func:`CaseCreate`, :aimms:func:`CaseDelete`.
