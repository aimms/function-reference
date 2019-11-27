.. aimms:procedure:: TestDataSource(Datasource, interactive, timeout)

.. _TestDataSource:

TestDataSource
==============

With the procedure :aimms:func:`TestDataSource` you can test for the presence of a
data source on a host computer, before reading or writing to it. If you
try to read or write to a non-existing data source, AIMMS will generate
error messages which may be confusing for your end users.

.. code-block:: aimms

    TestDataSource(
         Datasource,          ! (input) a string expression
         interactive,         ! (input/optional) an integer, default 1
         timeout              ! (input/optional) unit: seconds, default 30
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *interactive*
        When non-zero: if additional (logon) information is required a window is
        popped up. When zero: if additional (logon) information is required, the
        procedure will return immediately with the value 0.

    *timeout*
        When the timeout is expired the procedure TestDataSource will return
        with the value 0.

Return Value
------------

    The procedure returns 1 if the data source is present, or 0 otherwise.
    If the result is 0, the pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a
    proper error message.

.. seealso::

    The procedures :aimms:func:`TestDatabaseTable` and :aimms:func:`TestDatabaseColumn`.
