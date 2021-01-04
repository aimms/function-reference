.. aimms:set:: AllDefinedParameters

.. _AllDefinedParameters:

AllDefinedParameters
====================

The predefined set :aimms:set:`AllDefinedParameters` contains the names of all
defined parameters within an AIMMS model.

.. code-block:: aimms

        Set AllDefinedParameters {
            Subsetof   :  AllParameters;
            Index      :  IndexDefinedParameters;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDefinedParameters` is the collection of
    all parameters names with a non-empty ``Definition`` attribute within a
    particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    definitions of parameters declared in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllParameters`. Parameters are discussed in :doc:`non-procedural-language-components/parameter-declaration/parameter-declaration-and-attributes` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
