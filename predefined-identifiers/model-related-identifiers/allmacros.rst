.. aimms:set:: AllMacros

.. _AllMacros:

AllMacros
=========

The predefined set :aimms:set:`AllMacros` contains the names of all macros within
an AIMMS model.

.. code-block:: aimms

        Set AllMacros {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexMacros;
        }

Definition
----------

    The contents of the set :aimms:set:`AllMacros` is the collection of all
    *symbolic* macro names defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    macros in the **Model Explorer**.

.. seealso::

    Macros are discussed in :doc:`non-procedural-language-components/numerical-and-logical-expressions/macro-declaration-and-attributes` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
