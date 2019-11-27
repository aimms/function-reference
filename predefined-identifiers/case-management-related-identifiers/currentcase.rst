.. aimms:set:: CurrentCase

.. _CurrentCase:

CurrentCase
===========

The predefined element parameter :aimms:set:`CurrentCase` contains a reference to
the currently active case within an AIMMS project.

.. code-block:: aimms

        ElementParameter CurrentCase {
            Range      :  AllCases;
        }

Definition
----------

    The element parameter :aimms:set:`CurrentCase` contains an (integer) case
    reference (as an element of :aimms:set:`AllCases`) to the currently active case
    within an AIMMS project, or is empty if the active case is not named.

Updatability
------------

    The element parameter :aimms:set:`CurrentCase` is used in both data management
    styles ``Single_Data_Manager_file`` and ``Disk_files_and_folders``. When
    using ``Single_Data_Manager_file``, the value of :aimms:set:`CurrentCase` can
    only be modified by actively loading another case either in the **Data
    Manager**, through the **Data** menu, or using the functions :aimms:func:`CaseLoadCurrent`
    and :aimms:func:`CaseSaveAs`. When using ``Disk_files_and_folders``, the value of
    :aimms:set:`CurrentCase` can only be modified by actively loading or saving a
    case through the **Data** menu, or by using the functions :aimms:func:`CaseFileSetCurrent`,
    :aimms:func:`CaseCommandLoadAsActive`, :aimms:func:`CaseComandSave`, :aimms:func:`CaseComandSaveAs` or :aimms:func:`CaseCommandNew`.

.. seealso::

    The set :aimms:set:`AllCases`, the element parameter :aimms:set:`CurrentDataSet`. Loading and saving
    cases is discussed in full detail in Section 16.1 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
