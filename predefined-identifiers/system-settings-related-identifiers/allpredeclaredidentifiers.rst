.. aimms:set:: AllPredeclaredIdentifiers

.. _AllPredeclaredIdentifiers:

AllPredeclaredIdentifiers
=========================

The predefined set :aimms:set:`AllPredeclaredIdentifiers` contains the names of
all predeclared identifiers in AIMMS.

.. code-block:: aimms

        Set AllPredeclaredIdentifiers {
            SubsetOf   :  AllSymbols;
            Index      :  IndexPredeclaredIdentifiers;
        }

Definition
----------

    The contents of the set :aimms:set:`AllPredeclaredIdentifiers` is the collection
    of all predeclared identifier names.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The set :aimms:set:`AllSymbols`.
