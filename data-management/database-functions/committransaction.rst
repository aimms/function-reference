.. aimms:procedure:: CommitTransaction(None)

.. _CommitTransaction:

CommitTransaction
=================

By default, AIMMS places a transaction around any *single* ``WRITE``
statement to a database table. In this way, AIMMS makes sure that the
complete ``WRITE`` statement can be rolled back in the event of a
database error during the execution of that ``WRITE`` statement. With
the procedure :aimms:procedure:`CommitTransaction` you can commit all the changes to
the database (through ``WRITE`` statements or SQL queries) made since
the last call to ``StartTransaction``.

.. code-block:: aimms

    CommitTransaction

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 if the transaction was committed successfully,
    or 0 otherwise.

.. seealso::

    - The procedures :aimms:procedure:`StartTransaction`, :aimms:procedure:`RollbackTransaction`.
