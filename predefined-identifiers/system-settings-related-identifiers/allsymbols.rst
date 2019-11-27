.. aimms:set:: AllSymbols

.. _AllSymbols:

AllSymbols
==========

The predefined set :aimms:set:`AllSymbols` contains the names of identifiers,
predeclared identifiers, keywords, and intrinsics.

.. code-block:: aimms

        Set AllSymbols {
            Index      :  IndexSymbols;
            Definition :  {
                 AllPredeclaredIdentifiers + AllIdentifiers +
                 AllKeywords + AllIntrinsics
            }
        }

Definition
----------

    The contents of the set :aimms:set:`AllSymbols` is the collection of all
    identifiers, predeclared identifiers, keywords, and intrinsics.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    identifiers in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllPredeclaredIdentifiers`, :aimms:set:`AllKeywords`, and :aimms:set:`AllIntrinsics`.
