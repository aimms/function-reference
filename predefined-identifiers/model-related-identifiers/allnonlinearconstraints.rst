.. aimms:set:: AllNonLinearConstraints

.. _AllNonLinearConstraints:

AllNonLinearConstraints
=======================

The predefined set :aimms:set:`AllNonLinearConstraints` contains the names of all
non-linear constraints within an AIMMS model.

.. code-block:: aimms

        Set AllNonLinearConstraints {
            SubsetOf   :  AllConstraints;
            Index      :  IndexNonLinearConstraints;
        }

Definition
----------

    The contents of the set :aimms:set:`AllNonLinearConstraints` is the collection of
    all *symbolic* non-linear constraint names defined within a particular
    model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    non-linear constraints in the **Model Explorer**.

.. seealso::

    The set :aimms:set:`AllConstraints`.
