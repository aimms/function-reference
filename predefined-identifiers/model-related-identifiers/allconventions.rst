.. aimms:set:: AllConventions

.. _AllConventions:

AllConventions
==============

The predefined set :aimms:set:`AllConventions` contains the names of all
conventions defined within an AIMMS model.

.. code-block:: aimms

        Set AllConventions {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexConventions;
        }

Definition
----------

    The contents of the set :aimms:set:`AllConventions` is the collection of all
    conventions defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    conventions in the **Model Explorer**.

.. note::

    Element parameters into the set :aimms:set:`AllConventions` are typically used in
    the main model node to allow dynamic selection of the unit convention to
    which the model is subject.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`AllQuantities`. Conventions are discussed in full detail
    in :doc:`advanced-language-components/units-of-measurement/globally-overriding-units-through-conventions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
