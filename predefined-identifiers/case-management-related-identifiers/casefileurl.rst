.. aimms:set:: CaseFileURL

.. _CaseFileURL:

CaseFileURL
===========

The string parameter :aimms:set:`CaseFileURL` holds the url (i.e. the full path
name) of the file that corresponds to each element in :aimms:set:`AllCases`.

.. code-block:: aimms

        StringParameter CaseFileURL {
            IndexDomain  :  AllCases;
        }

Definition
----------

    The contents of the set :aimms:set:`AllCases` is the collection of (integer)
    references to all case files that have been loaded or saved during a
    specific session of your AIMMS project. The string parameter
    :aimms:set:`CaseFileURL` helps you to get the location of each of these cases.

Updatability
------------

    The contents of the set :aimms:set:`AllCases` as well as their corresponding
    values in :aimms:set:`CaseFileURL` are maintained by AIMMS itself and cannot be
    modified directly. They are modified when you load or save cases, or
    through the function :aimms:func:`CaseFileURLtoElement`.

.. note::

    -  This predeclared identifier is only relevant if the project option
       ``Data_Management_style`` is set to ``Disk_files_and_folders``.

    -  The integer case references stored in the set :aimms:set:`AllCases` are only
       guaranteed to be unique within a single AIMMS session.

.. seealso::

    The set :aimms:set:`AllCases` and the function :aimms:func:`CaseFileURLtoElement`.
