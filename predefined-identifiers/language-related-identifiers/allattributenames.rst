.. aimms:set:: AllAttributeNames

.. _AllAttributeNames:

AllAttributeNames
=================

The predefined set :aimms:set:`AllAttributeNames` contains the names of all
possible identifier attributes.

.. code-block:: aimms

        Set AllAttributeNames {
            Index      :  IndexAttributeNames;
        }

Definition
----------

    The predefined set :aimms:set:`AllAttributeNames` contains the names of all
    possible identifier attributes.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    -  The sets :aimms:set:`AllIdentifierTypes`, and :aimms:set:`AllSuffixNames`.

    -  Model edit functions, see :doc:`advanced-language-components/model-structure-and-modules/runtime-libraries-and-the-model-edit-functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The functions :aimms:func:`me::AllowedAttribute` and :aimms:func:`IdentifierAttributes`.
