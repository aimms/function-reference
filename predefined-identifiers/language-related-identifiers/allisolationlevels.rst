.. aimms:set:: AllIsolationLevels

.. _AllIsolationLevels:

AllIsolationLevels
==================

The predefined set :aimms:set:`AllIsolationLevels` contains the supported
isolation levels for a database transaction, as started through the
procedure :aimms:procedure:`StartTransaction`.

.. code-block:: aimms

        Set AllIsolationLevels {
            Index      :  IndexIsolationLevels;
            Definition :  {
                data { ReadUncommitted, ReadCommitted,
                       RepeatableRead, Serializable }
            }
        }

Definition
----------

    The predefined set :aimms:set:`AllIsolationLevels` contains the supported
    isolation levels for a database transaction. They are:

    -  ``ReadUncommitted``: a transaction operating at this level can see
       uncommitted changes made by other transactions,

    -  ``ReadCommitted`` (default): a transaction operating at this level
       cannot see changes made by other transactions until those
       transactions are committed,

    -  ``RepeatableRead``: a transaction operating at this level is
       guaranteed not to see any changes made by other transactions in
       values it has already read during the transaction, and

    -  ``Serializable``: a transaction operating at this level guarantees
       that all concurrent transactions interact only in ways that produce
       the same effect as if each transaction were entirely executed one
       after the other.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Not all database servers may support all of these isolation levels, and
    may cause the call to ``StartTransaction`` to fail.

.. seealso::

    The function :aimms:procedure:`StartTransaction`.
