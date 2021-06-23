.. aimms:set:: DiskWindowVoid

.. _DiskWindowVoid:

DiskWindowVoid
==============

The predefined set :aimms:set:`DiskWindowVoid` defines the set of possible
devices of file identifiers.

.. code-block:: aimms

        Set DiskWindowVoid {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexDiskWindowVoid;
            Definition :  data { disk, window, void };
        }

Definition
----------

    The predefined set :aimms:set:`DiskWindowVoid` defines the set of possible
    devices which can be entered in the ``Device`` attribute of a ``File``
    identifier.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`DiskWindowVoid` can be entered in the
    ``Device`` attribute of ``File`` identifiers to allow dynamic device
    changes for a file.

.. seealso::

    The set :aimms:set:`AllValueKeywords`. File identifiers are discussed in :doc:`data-communication-components/text-reports-and-output-listing/the-file-declaration` of the
     Language Reference.
