.. aimms:set:: AllDefinedSets

.. _AllDefinedSets:

AllDefinedSets
==============

The predefined set :aimms:set:`AllDefinedSets` contains the names of all defined
sets within an AIMMS model.

.. code-block:: aimms

        Set AllDefinedSets {
            SubsetOf   :  AllSets;
            Index      :  IndexDefinedSets;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDefinedSets` is the collection of all set
    names with a non-empty ``Definition`` attribute within a particular
    model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    definitions of sets declared in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllSets`. Sets are discussed in Section 3.2 of the Language
    Reference.
