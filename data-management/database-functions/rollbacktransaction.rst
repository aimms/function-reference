.. aimms:procedure:: RollbackTransaction(None)

.. _RollbackTransaction:

RollbackTransaction
===================

By default, AIMMS places a transaction around any *single* ``WRITE``
statement to a database table. In this way, AIMMS makes sure that the
complete ``WRITE`` statement can be rolled back in the event of a
database error during the execution of that ``WRITE`` statement. With
the procedure :aimms:procedure:`RollbackTransaction` you can rollback (undo) all the
changes to the database (through ``WRITE`` statements or SQL queries)
made since the last call to ``StartTransaction``.

.. code-block:: aimms

    RollbackTransaction

Arguments
---------

    *None*

Return Value
------------

    The procedure returns 1 if the transaction was rolled back successfully,
    or 0 otherwise.

.. seealso::

    The procedures :aimms:procedure:`StartTransaction`, :aimms:procedure:`RollbackTransaction`.
