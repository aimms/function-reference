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
    :doc:`data-communication-components/data-initialization-verification-and-control/data-control`, the ``READ`` and ``WRITE`` statements in :doc:`data-communication-components/the-read-and-write-statements/syntax-of-the-read-and-write-statements`, and
    the ``DISPLAY`` statement in :doc:`data-communication-components/text-reports-and-output-listing/the-display-statement` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
