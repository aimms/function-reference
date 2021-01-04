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

    The set :aimms:set:`AllSymbols`. Data control statements are discussed in :doc:`data-communication-components/data-initialization-verification-and-control/data-control`, 
    the ``READ`` and ``WRITE`` statements in :doc:`data-communication-components/the-read-and-write-statements/syntax-of-the-read-and-write-statements`, and the
    ``DISPLAY`` statement in :doc:`data-communication-components/text-reports-and-output-listing/the-display-statement` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__. Working
    with the set :aimms:set:`AllIdentifiers` is described in more detail in :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers`.
