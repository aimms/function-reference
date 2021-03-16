.. aimms:set:: CurrentCaseFileContentType

.. _CurrentCaseFileContentType:

CurrentCaseFileContentType
==========================

The predefined element parameter :aimms:set:`CurrentCaseFileContentType` contains
the references to a case file content, corresponding to the most
recently loaded or saved case file.

.. code-block:: aimms

        ElementParameter CurrentCaseFileContentType {
            Range        :  AllCaseFileContentTypes;
        }

Definition
----------

    The value of :aimms:set:`CurrentCaseFileContentType` is a references to a subset
    of :aimms:set:`AllIdentifiers`, which corresponds to the data that is stored in
    the most recently loaded or saved case file. This subset is also used to
    determine whether any data needs to be saved for the current case,
    before loading another case file.

Updatability
------------

    The value of the element parameter can be freely modified. The standard
    case management functionality updates the value itself whenever a case
    file is loaded or saved.

.. note::

    -  This predeclared identifier is only relevant if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

.. seealso::

    The set :aimms:set:`AllCaseFileContentTypes`.
