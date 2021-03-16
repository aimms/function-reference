.. aimms:set:: CurrentDefaultCaseType

.. _CurrentDefaultCaseType:

CurrentDefaultCaseType
======================

The predefined element parameter :aimms:set:`AllCaseTypes` contains the name of
the current default case type.

.. code-block:: aimms

        ElementParameter CurrentDefaultCaseType {
            Range      :  AllCaseTypes;
        }

Definition
----------

    The value of the element parameter :aimms:set:`CurrentDefaultCaseType`, if
    non-empty, restricts the selection of visible cases to the cases of the
    specified case type in the **Load Case** dialog box. In addition, a
    non-empty value of :aimms:set:`CurrentDefaultCaseType` presets the case type to
    the specified case type in the **Save Case** dialog box, and removes the
    end-user's capability to modify the case type interactively.

Updatability
------------

    The value of the element parameter can be modified both in the model and
    in the graphical end-user interface.

.. note::

    This identifier is only relevant when the chosen
    ``Data_Management_style`` is ``single_data_manager_file``.
