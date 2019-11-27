.. aimms:set:: AllIntegerVariables

.. _AllIntegerVariables:

AllIntegerVariables
===================

The predefined set :aimms:set:`AllIntegerVariables` contains the names of all
integer variables within an AIMMS model.

.. code-block:: aimms

        Set AllIntegerVariables {
            SubsetOf   :  AllVariables;
            Index      :  IndexIntegerVariables;
        }

Definition
----------

    The contents of the set :aimms:set:`AllIntegerVariables` is the collection of all
    *symbolic* variable names with as range a subset of ``Integers`` defined
    within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    integer variables in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllVariables`, :aimms:set:`Integers`.
