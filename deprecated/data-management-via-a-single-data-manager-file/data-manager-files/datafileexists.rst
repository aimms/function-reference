.. aimms:procedure:: DataFileExists(datafile)

.. _DataFileExists:

DataFileExists
==============

With the procedure :aimms:func:`DataFileExists` you can check whether a specific
element from the set ``AllDataFiles`` still refers to a valid case or
dataset. Especially when multiple users have access to the same data
file, an element may become invalid.

.. code-block:: aimms

    DataFileExists(
            datafile      ! (input) element in the set AllDataFiles
            )

Arguments
---------

    *datafile*
        An element in the set ``AllDataFiles``, ``AllCases`` or ``AllDataSets``.

Return Value
------------

    The procedure returns 1 if the given datafile still exists, and 0
    otherwise.

.. note::

    -  This function is only applicable if the project option
       ``Data_Management_style`` is set to ``Single_Data_Manager_file``.

    -  Note that ``AllCases`` and ``AllDataSets`` are subsets of
       ``AllDataFiles``.

.. seealso::

    The procedure :aimms:func:`DataFileGetName`.
