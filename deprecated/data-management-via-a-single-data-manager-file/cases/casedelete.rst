.. aimms:procedure:: CaseDelete(case)

.. _CaseDelete:

CaseDelete
==========

The procedure :aimms:func:`CaseDelete` deletes a specific case node from the Data
Management tree.

.. code-block:: aimms

    CaseDelete(
              case    ! (input) element parameter into AllCases
              )

Arguments
---------

    *case*
        An element parameter into :aimms:set:`AllCases`, representing the case that you want
        to delete.

Return Value
------------

    The procedure returns 1 if the case is deleted successfully, or 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  If the option ``Data_Management_style`` is set to
       ``disk_files_and_folders``, please use the function :aimms:func:`FileDelete`
       instead.

.. seealso::

    The procedure :aimms:func:`CaseFind`.
