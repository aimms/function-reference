.. aimms:set:: AllBasicValues

.. _AllBasicValues:

AllBasicValues
==============

The predefined set :aimms:set:`AllBasicValues` contains the names of all basic
values available in AIMMS.

.. code-block:: aimms

        Set AllBasicValues {
            Index      :  IndexBasicValues;
            Definition :  data { NonBasic, Basic, SuperBasic };
        }

Definition
----------

    The set :aimms:set:`AllBasicValues` contains the names of all basic values in
    AIMMS.

Updatability
------------

    The contents of the set cannot be modified.
