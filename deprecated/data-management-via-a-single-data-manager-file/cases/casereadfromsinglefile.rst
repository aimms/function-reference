.. aimms:procedure:: CaseReadFromSingleFile(inputFileName)

.. _CaseReadFromSingleFile:

CaseReadFromSingleFile
======================

The procedure :aimms:func:`CaseReadFromSingleFile` reads the data from a single
case file on disk.

.. code-block:: aimms

    CaseReadFromSingleFile(
            inputFileName               ! (input) scalar string expression
            )

Arguments
---------

    *inputFileName*
        A string expression holding the path and name of the input file.

Return Value
------------

    The procedure returns 1 on success, or 0 otherwise.

.. seealso::

    The procedures :aimms:func:`CaseWriteToSingleFile`, :aimms:func:`CaseSave`.
