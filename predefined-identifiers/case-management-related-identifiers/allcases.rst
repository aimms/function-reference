.. aimms:set:: AllCases

.. _AllCases:

AllCases
========

The predefined set :aimms:set:`AllCases` contains the references to all cases
that are currently available in the AIMMS project.

.. code-block:: aimms

        Set AllCases {
            SubsetOf   :  AllDataFiles;
            Index      :  IndexCases;
        }

Definition
----------

    The set :aimms:set:`AllCases` is used in both data management styles
    ``Single_Data_Manager_file`` and ``Disk_files_and_folders``. When using
    ``Single_Data_Manager_file``, the contents of the set :aimms:set:`AllCases` is
    the collection of (integer) references to all cases stored within the
    data manager file currently loaded within an AIMMS project. When using
    ``Disk_files_and_folders``, the contents of the set :aimms:set:`AllCases` is the
    collection of (integer) references to all case files that have been
    referenced thus far. Each newly opened or saved case file is
    automatically added to this set.

Updatability
------------

    The contents of the set can only be modified implicitly by using the
    various features of the Data Management tool, by executing any of the
    Data menu commands or by using the specific case or dataset functions.

.. note::

    If the data management style is set to ``Single_Data_Manager_file``.

    -  Further information about the integer case references can be obtained
       through the functions :aimms:func:`DataFileGetAcronym`, :aimms:func:`DataFileGetDescription`, :aimms:func:`DataFileGetGroup`, :aimms:func:`DataFileGetName`,
       :aimms:func:`DataFileGetOwner`, :aimms:func:`DataFileGetPath` and :aimms:func:`DataFileGetTime`.

    -  The integer case references stored in the set :aimms:set:`AllCases` are only
       guaranteed to be unique within a single AIMMS session, and,
       furthermore, only within the context of a single data manager file
       associated with a project. As a consequence, additional case
       information retrieved through the functions listed above must be
       refreshed after opening another data manager file.

    If the data management style is set to ``Disk_files_and_folders``.

    -  The corresponding location on disk of any element in the set
       :aimms:set:`AllCases` can be obtained through the predeclared identifier
       :aimms:set:`CaseFileURL`.

    -  The integer case references stored in the set :aimms:set:`AllCases` are only
       guaranteed to be unique within a single AIMMS session and depend on
       the order in which case files are accessed.

.. seealso::

    The set :aimms:set:`AllDataFiles`. Accessing cases from within an AIMMS model is
    discussed in full detail in :doc:`data-management/case-management/managing-multiple-case-selections`.
