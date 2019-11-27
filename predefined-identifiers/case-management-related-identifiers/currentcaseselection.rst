.. aimms:set:: CurrentCaseSelection

.. _CurrentCaseSelection:

CurrentCaseSelection
====================

The predefined set :aimms:set:`CurrentCaseSelection` contains the current
multiple case selection within an AIMMS project.

.. code-block:: aimms

        Set CurrentCaseSelection {
            SubsetOf   :  AllCases;
            Index      :  IndexCurrentCaseSelection;
        }

Definition
----------

    The contents of the set :aimms:set:`CurrentCaseSelection` is the collection of
    (integer) case references (as elements of :aimms:set:`AllCases`) that is currently
    part of the multiple case selection.

Updatability
------------

    The contents of the set can be modified through the **Data-Multiple
    Cases** menu, by calling the function :aimms:func:`CaseSelectMultiple`, or programmatically
    through a direct assignment within the model.

.. seealso::

    The set :aimms:set:`AllCases`. Working with multiple cases is discussed in full
    detail in Section 16.2 of the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
