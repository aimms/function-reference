.. aimms:procedure:: DirectSQL(Datasource, SQLstatement)

.. _DirectSQL:

DirectSQL
=========

With the procedure :aimms:procedure:`DirectSQL` you can directly execute SQL statements
within a data source.

.. code-block:: aimms

    DirectSQL(
         Datasource,         ! (input) a string expression
         SQLstatement        ! (input) a string expression
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *SQLstatement*
        A string containing the SQL statement that must be executed within the
        data source.

Return Value
------------

    The procedure returns 1 if the SQL statement is executed successfully,
    or 0 if the execution failed. In case of failure, the corresponding
    error message can be obtained through the predefined string parameter
    :aimms:set:`CurrentErrorMessage`.

    .. note::

        -   If the SQL statement also produces a result set, then this set is
            ignored by AIMMS.

        -   Note that the SQL dialect used by, for instance, Oracle, SQL Server
            and Microsoft Access may differ. If a call to :aimms:procedure:`DirectSQL` fails
            because of such differences, you should inspect
            ``CurrentErrorMessage`` for further details.

.. seealso::

    -   Calling stored procedures and executing SQL queries through AIMMS
        ``DATABASE PROCEDURES`` is discussed in :doc:`data-communication-components/communicating-with-databases/executing-stored-procedures-and-sql-queries` of the Language Reference.
