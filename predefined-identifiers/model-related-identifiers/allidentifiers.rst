.. aimms:set:: AllIdentifiers

.. _AllIdentifiers:

AllIdentifiers
==============

The predefined set :aimms:set:`AllIdentifiers` contains the names of all
identifiers declared within an AIMMS model.

.. code-block:: aimms

        Set AllIdentifiers {
            SubsetOf   :  AllSymbols;
            Index      :  IndexIdentifiers, SecondIndexIdentifiers;
        }

Definition
----------

    The contents of the set :aimms:set:`AllIdentifiers` is the collection of all
    identifier and section names declared within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    identifiers in the **Model Explorer**.

.. note::

    Subsets of :aimms:set:`AllIdentifiers` are occassionally used in ``READ``,
    ``WRITE`` or ``DISPLAY`` statements to indicate the set of identifiers
    to be read or written, as well as in data control statements such as
    ``EMPTY`` and ``CLEANUP``. It also serves as the root set of the other
    (typed) identifier sets, which can be used throughout an AIMMS project.

.. seealso::

    The set :aimms:set:`AllSymbols`. Data control statements are discussed in Section
    25.3, the ``READ`` and ``WRITE`` statements in Section 26.2, and the
    ``DISPLAY`` statement in Section 31.3 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__. Working
    with the set :aimms:set:`AllIdentifiers` is described in more detail in Section
    25.4.
