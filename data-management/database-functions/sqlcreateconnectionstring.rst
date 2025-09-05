.. aimms:function:: SQLCreateConnectionString(DatabaseInterface, DriverName[, ServerName][, DatabaseName][, UserId], Password[, AdditionalConnectionParameters])

.. _SQLCreateConnectionString:

SQLCreateConnectionString
=========================

The function :aimms:func:`SQLCreateConnectionString` assists you in creating a
*connection string*, which can be used to specify the ``Data source``
attribute of database tables, functions or procedures. Using a
connection string to connect to a data source, makes it possible to keep
your database passwords hidden.

.. code-block:: aimms

    SQLCreateConnectionString(
         DatabaseInterface,                ! (input) an element expression
         DriverName,                       ! (input) a string expression
         [ServerName],                     ! (optional) a string expression
         [DatabaseName],                   ! (optional) a string expression
         [UserId],                         ! (optional) a string expression
         [Password],                       ! (optional) a string expression
         [AdditionalConnectionParameters]  ! (optional) a string expression
         )

Arguments
---------

    *DatabaseInterface*
        Element value into the set AllDatabaseInterfaces. Currently, this set
        contains only the value ``'ODBC'``.

    *DriverName*
        A string containing the name of the ODBC driver to which you want to
        connect using the resulting connection string. See the functions
        :aimms:func:`SQLNumberOfDrivers` and :aimms:func:`SQLDriverName` on how to obtain the driver/provider name.

    *ServerName (optional)*
        A string containing the name of the server on which the data source to
        connect to is hosted.

    *DatabaseName (optional)*
        A string containing the name of the database to which you want to
        connect.

    *UserId (optional)*
        A string containing the user id with which to login on the datasource.

    *Password*
        A string containing the password to use when logging in on the
        datasource. The password will not be part of the resulting string, but
        will be stored internally, making it possible to communicate by means of
        the connectionstring without revealing the credentials.

    *AdditionalConnectionParameters (optional)*
        A string containing any additional connection parameters to be passed to
        the data source using the resulting connection string. These additional
        parameters should be specified in the form ``KEYWORD=VALUE``, and these
        keyword/value pairs must be separated by semi-colons. Different
        drivers/providers accept different keywords. Please refer to the
        documentation of your ODBC driver for more information.

Return Value
------------

    The function returns a connection string, which can be used to connect
    to a data source on your system.

    .. note::

        The returned connection string can be used as the data source attribute
        of database related identifiers in AIMMS. Also, it can be used in
        database related functions (e.g. ``SQLDirect``) as the ``Datasource``
        argument.

.. seealso::

    - The functions :aimms:func:`SQLNumberOfDrivers` and :aimms:func:`SQLDriverName`.
