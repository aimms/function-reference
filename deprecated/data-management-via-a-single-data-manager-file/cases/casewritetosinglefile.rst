.. aimms:procedure:: CaseWriteToSingleFile(outputFileName)

.. _CaseWriteToSingleFile:

CaseWriteToSingleFile
=====================

The procedure :aimms:func:`CaseWriteToSingleFile` writes the current data to a
case file on disk.

.. code-block:: aimms

    CaseWriteToSingleFile(
            outputFileName               ! (input) scalar string expression
            )

Arguments
---------

    *outputFileName*
        A string expression holding the path and name of the output file.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  The procedure :aimms:func:`CaseWriteToSingleFile` uses the current case type to
       determine which data should be written. This is usually the case type
       of the last loaded case. If you want to make sure that a specific
       case type is used, you can preset the case type via the predefined
       element parameter ``CurrentDefaultCaseType``.

    The files written by :aimms:func:`CaseWriteToSingleFile` can only be read by
    ``CaseReadFromSingleFile``.

.. seealso::

    The procedures :aimms:func:`CaseReadFromSingleFile`, :aimms:func:`CaseSave`.
