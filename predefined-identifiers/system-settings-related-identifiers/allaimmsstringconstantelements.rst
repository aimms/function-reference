.. aimms:set:: AllAimmsStringConstantElements

.. _AllAimmsStringConstantElements:

AllAimmsStringConstantElements
==============================

The predefined set :aimms:set:`AllAimmsStringConstantElements` contains the
elements for which the predeclared string parameter :aimms:set:`AimmsStringConstants` has a
value.

.. code-block:: aimms

        Set AllAimmsStringConstantElements {
            Index      :  IndexAimmsStringConstantElements;
        }

Definition
----------

    This set is fixed to ``{ Platform, Architecture, Flavor }``.
