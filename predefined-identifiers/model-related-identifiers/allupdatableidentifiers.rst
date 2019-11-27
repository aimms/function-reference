.. aimms:set:: AllUpdatableIdentifiers

.. _AllUpdatableIdentifiers:

AllUpdatableIdentifiers
=======================

The predefined set :aimms:set:`AllUpdatableIdentifiers` contains the names of the
identifiers that are, in principle, updatable.

.. code-block:: aimms

        Set AllUpdatableIdentifiers {
            SubsetOf     :  AllIdentifiers;
            Index        :  IndexUpdatableIdentifiers;
            InitialData  :  {
                ( AllSets - AllDefinedSets ) +
                ( AllParameters - AllDefinedParameters )
            }
        }

Definition
----------

    The set :aimms:set:`AllUpdatableIdentifiers` contains the names of the model
    identifiers that are, in principle, considered updatable by AIMMS.

Updatability
------------

    The contents of :aimms:set:`AllUpdatableIdentifiers` can be modified
    programmatically from within an AIMMS model. The set cannot be updated
    from within the end-user interface.

.. note::

    -  The set :aimms:set:`AllUpdatableIdentifiers` determines which identifiers are
       updatable *in principle*. Which identifiers in
       :aimms:set:`AllUpdatableIdentifiers` can *actually* be modified within the
       graphical end-user interface is determined by the set :aimms:set:`CurrentInputs`.

    -  By default, variables are considered not updatable by AIMMS. If you
       want to allow your end-users to update some or all variables from
       within the end-user interface, you can accomplish this by adding
       these variables to both the sets :aimms:set:`AllUpdatableIdentifiers` and
       :aimms:set:`CurrentInputs`.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`CurrentInputs`.
