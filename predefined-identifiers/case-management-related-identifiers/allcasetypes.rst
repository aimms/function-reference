.. aimms:set:: AllCaseTypes

.. _AllCaseTypes:

AllCaseTypes
============

The predefined set :aimms:set:`AllCaseTypes` contains the names of all case types
declared within an AIMMS project.

.. code-block:: aimms

        Set AllCaseTypes {
            Index      :  IndexCaseTypes;
        }

Definition
----------

    The contents of the set :aimms:set:`AllCaseTypes` is the collection of all case
    types defined within the **Data Management Setup** tool of a project.

Updatability
------------

    The contents of the set can only be modified by adding or deleting case
    types in the **Data Management Setup** tool.

.. note::

    -  The function :aimms:func:`CaseGetType` returns the case type of a case as an element
       of the set :aimms:set:`AllCaseTypes`. The identifiers and data categories
       associated with a case type can be obtained through the functions
       :aimms:func:`CaseTypeContents` and :aimms:func:`CaseTypeCategories`. The default case type of a case when saving
       it is set through the predefined element parameter :aimms:set:`CurrentDefaultCaseType`.

    -  This identifier is only relevant when the chosen
       ``Data_Management_style`` is ``single_data_manager_file``.
