.. aimms:set:: AllIndices

.. _AllIndices:

AllIndices
==========

The predefined set :aimms:set:`AllIndices` contains the names of all indices
defined within an AIMMS model.

.. code-block:: aimms

        Set AllIndices {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexIndices;
        }

Definition
----------

    The contents of the set :aimms:set:`AllIndices` is the collection of all indices
    defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding indices to or
    deleting indices from sets within the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllSets`, :aimms:set:`AllIdentifiers`. Sets and their corresponding indices are
    discussed in Section 3.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
