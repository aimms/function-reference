.. aimms:set:: AllCaseFileContentTypes

.. _AllCaseFileContentTypes:

AllCaseFileContentTypes
=======================

The predefined set :aimms:set:`AllCaseFileContentTypes` contains the references
to all case file content types that can be used within a particular
AIMMS project.

.. code-block:: aimms

        Set AllCaseFileContentTypes {
            SubsetOf   :  AllSubsetsOfAllIdentifiers;
            Index      :  IndexCaseFileContentTypes;
        }

Definition
----------

    An element in the set :aimms:set:`AllCaseFileContentTypes` is a subset of
    :aimms:set:`AllIdentifiers`. Such a subset defines the identifiers that are
    stored in a case file.

Updatability
------------

    The contents of this set can be freely modified. By default, it only
    contains the element :aimms:set:`AllIdentifiers`. If your project uses multiple
    types of case files with different content, you should replace the
    default content of this set with all content types applicable to your
    project.

.. note::

    -  This predeclared identifier is only relevant if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  If this set contains more than one element, the dialog box for saving
       a case file will show an additional drop down box, in which the user
       can select the case content type to be used for saving.

.. seealso::

    The set :aimms:set:`AllSubsetsOfAllIdentifiers`.
