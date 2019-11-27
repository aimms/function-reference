.. aimms:set:: AllSets

.. _AllSets:

AllSets
=======

The predefined set :aimms:set:`AllSets` contains the names of all sets within an
AIMMS model.

.. code-block:: aimms

        Set AllSets {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexSets;
        }

Definition
----------

    The contents of the set :aimms:set:`AllSets` is the collection of all set names
    declared within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting sets
    in the **Model Explorer**.

.. note::

    Subsets of :aimms:set:`AllSets` are occassionally used in ``READ``, ``WRITE`` or
    ``DISPLAY`` statements to indicate the set of sets to be read or
    written, as well as in data control statements such as ``EMPTY``,
    ``CLEANUP`` and ``CLEANUPDEPENDENTS``.

.. seealso::

    The sets :aimms:set:`AllDefinedSets`, :aimms:set:`AllIdentifiers`. Data control statements are discussed in
    Section 25.3, the ``READ`` and ``WRITE`` statements in Section 26.2, and
    the ``DISPLAY`` statement in Section 31.3 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
