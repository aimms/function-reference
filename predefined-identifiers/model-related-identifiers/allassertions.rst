.. aimms:set:: AllAssertions

.. _AllAssertions:

AllAssertions
=============

The predefined set :aimms:set:`AllAssertions` contains the names of all
assertions within an AIMMS model.

.. code-block:: aimms

        Set AllAssertions {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexAssertions;
        }

Definition
----------

    The contents of the set :aimms:set:`AllAssertions` is the collection of all
    assertion names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    assertions in the **Model Explorer**.

.. note::

    The set :aimms:set:`AllAssertions` or subsets thereof are typically used in the
    ``ASSERT`` statement in an AIMMS model.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`. Assertions are discussed in :doc:`data-communication-components/data-initialization-verification-and-control/assertions` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
