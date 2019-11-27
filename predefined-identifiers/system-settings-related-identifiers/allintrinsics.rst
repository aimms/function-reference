.. aimms:set:: AllIntrinsics

.. _AllIntrinsics:

AllIntrinsics
=============

The predefined set :aimms:set:`AllIntrinsics` contains the names of all standard
AIMMS functions and operators.

.. code-block:: aimms

        Set AllIntrinsics {
            SubsetOf   :  AllSymbols;
            Index      :  IndexIntrinsics;
        }

Definition
----------

    The contents of the set :aimms:set:`AllIntrinsics` is the collection of all
    standard functions and operators.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The set :aimms:set:`AllSymbols`.
