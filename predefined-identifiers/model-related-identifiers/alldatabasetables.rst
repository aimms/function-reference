.. aimms:set:: AllDatabaseTables

.. _AllDatabaseTables:

AllDatabaseTables
=================

The predefined set :aimms:set:`AllDatabaseTables` contains the names of all
database tables declared within an AIMMS model.

.. code-block:: aimms

        Set AllDatabaseTables {
            SubsetOf   :  AllIdentifiers;
            Index      :  IndexDatabaseTables;
        }

Definition
----------

    The contents of the set :aimms:set:`AllDatabaseTables` is the collection of all
    database tables declared within a particular model.

Updatability
------------

    The contents of the set can only be modified by adding or deleting
    database tables in the **Model Explorer**.

.. seealso::

    The sets :aimms:set:`AllIdentifiers`. Database tables are discussed in :doc:`data-communication-components/communicating-with-databases/the-databasetable-declaration` of the
     Language Reference.
