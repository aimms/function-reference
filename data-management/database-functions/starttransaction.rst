.. aimms:procedure:: StartTransaction(IsolationLevel)

.. _StartTransaction:

StartTransaction
================

By default, AIMMS places a transaction around any *single* ``WRITE``
statement to a database table. In this way, AIMMS makes sure that the
complete ``WRITE`` statement can be rolled back in the event of a
database error during the execution of that ``WRITE`` statement. With
the procedure :aimms:procedure:`StartTransaction` you can manually initiate a database
transaction which can contain multiple ``READ``, ``WRITE`` statements
and SQL queries.

.. code-block:: aimms

    StartTransaction(
         IsolationLevel         ! (optional) an element expression
         )

Arguments
---------

    *IsolationLevel*
        Element value into the set :aimms:set:`AllIsolationLevels`, indicating the isolation level at
        which the transaction has to take place. If omitted, defaults to
        ``'ReadCommitted'``.

Return Value
------------

    The procedure returns 1 if the transaction was started successfully, or
    0 otherwise.

.. note::

    You cannot call :aimms:procedure:`StartTransaction` recursively, i.e. you must call
    ``CommitTransaction`` or ``RollbackTransaction`` prior to the next call
    to :aimms:procedure:`StartTransaction`.

.. seealso::

    - The procedures :aimms:procedure:`CommitTransaction` and :aimms:procedure:`RollbackTransaction`.
