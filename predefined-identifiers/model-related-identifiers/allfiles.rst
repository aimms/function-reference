.. aimms:set:: AllFiles

.. _AllFiles:

AllFiles
========

The predefined set :aimms:set:`AllFiles` contains the names of all files declared
within an AIMMS model.

.. code-block:: aimms

        Set AllFiles {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexFiles;
        }

Definition
----------

    The contents of the set :aimms:set:`AllFiles` is the collection of all file
    identifiers defined within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting file
    identifiers in the **Model Explorer**.

.. note::

    The set :aimms:set:`AllFiles` is the range of the element parameter :aimms:set:`CurrentFile`.

.. seealso::

    The element parameter :aimms:set:`CurrentFile`. Files are discussed in Section 31.1 of
    the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
