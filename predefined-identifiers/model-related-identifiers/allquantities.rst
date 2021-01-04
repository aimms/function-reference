.. aimms:set:: AllQuantities

.. _AllQuantities:

AllQuantities
=============

The predefined set :aimms:set:`AllQuantities` contains the names of all
quantities defined within an AIMMS model.

.. code-block:: aimms

        Set AllQuantities {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexQuantities;
        }

Definition
----------

    The contents of the set :aimms:set:`AllQuantities` is the collection of all
    quantities defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    quantities in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllConventions`. Quantities are discussed in full detail
    in :doc:`advanced-language-components/units-of-measurement/the-quantity-declaration` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
