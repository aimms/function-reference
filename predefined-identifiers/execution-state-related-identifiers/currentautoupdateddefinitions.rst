.. aimms:set:: CurrentAutoUpdatedDefinitions

.. _CurrentAutoUpdatedDefinitions:

CurrentAutoUpdatedDefinitions
=============================

The predefined set :aimms:set:`CurrentAutoUpdatedDefinitions` contains the names
of the defined identifiers whose values are updated automatically upon
change of their input values when displayed in the graphical end-user
interface.

.. code-block:: aimms

        Set CurrentAutoUpdatedDefinitions {
            SubsetOf     :  AllIdentifiers;
            Index        :  IndexCurrentAutoUpdatedDefinitions;
            InitialData  :  AllDefinedSets + AllDefinedParameters;
        }

Definition
----------

    The set :aimms:set:`CurrentAutoUpdatedDefinitions` contains the names of the
    defined identifiers whose values are updated automatically upon change
    of their input values when displayed in the graphical end-user
    interface.

Updatability
------------

    The contents of :aimms:set:`CurrentAutoUpdatedDefinitions` can be modified
    programmatically from within an AIMMS model. The set cannot be modified
    from within the end-user interface.

.. note::

    By default, all defined parameters and sets are immediately updated in a
    graphical display whenever their input values are modified. In some
    cases, however, this behavior can be unwanted, for instance if each
    single data change by an end-user leads to a long re-evaluation of a
    defined identifier which is also displayed on the same page. In such
    cases, you can remove the defined identifier at hand from the set
    :aimms:set:`CurrentAutoUpdatedDefinitions` and explicitly update the identifier
    when you see fit, either by calling the ``UPDATE`` statement, or by
    updating the identifier on page entry, upon data change, or through a
    button action.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`, :aimms:set:`CurrentInputs`. The ``UPDATE`` statement and the set
    :aimms:set:`CurrentAutoUpdatedDefinitions` are discussed in more detail in
    Section 7.3 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
