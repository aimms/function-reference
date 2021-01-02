.. aimms:set:: OnOff

.. _OnOff:

OnOff
=====

The predefined set :aimms:set:`OnOff` defines the set of possibilities the
``PageMode`` suffix of ``File`` identifiers.

.. code-block:: aimms

        Set OnOff {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexOnOff;
            Definition :  data { on, off };
        }

Definition
----------

    The set :aimms:set:`OnOff` defines the set of possibilities the ``PageMode``
    suffix of ``File`` identifiers.

Updatability
------------

    The contents of the set :aimms:set:`OnOff` cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`OnOff` assigned to be ``PageMode``
    suffix of a ``File`` identifier can be used to dynamically change the
    page mode of a file.

.. seealso::

    The set :aimms:set:`AllValueKeywords`. The ``PageMode`` suffix of ``FILE`` identifiers is
    discussed in full detail in :doc:`data-communication-components/text-reports-and-output-listing/structuring-a-page-in-page-mode`
