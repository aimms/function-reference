.. aimms:function:: GetDataSourceProperty(Datasource, Property)

.. _GetDataSourceProperty:

GetDataSourceProperty
=====================

With the function :aimms:func:`GetDataSourceProperty` you can retrieve some
meta-data about a datasource. This is useful, when you don't know
beforehand what kind of datasource will be linked with your AIMMS
project. It allows you to provide datasource-specific SQL Queries in
your project, which you can then call based upon what datasource is
actually linked to your project. For example, you can determine with
this function that the actual datasource is an Oracle database, and then
execute some Oracle-specific SQL Queries.

.. code-block:: aimms

    GetDataSourceProperty(
         Datasource,          ! (input) a string expression
         Property,            ! (input) an element in the set
                                  AllDataSourceProperties
         )

Arguments
---------

    *Datasource*
        A string containing the name of a data source.

    *Property*
        An element parameter in the set :aimms:set:`AllDataSourceProperties`.

Return Value
------------

    The function returns a string with the requested datasource property in
    it.

.. note::

    The actual string which is returned depends on the datasource used. As
    an example of the datasource dependency of the function: retrieving the
    property ``SQL_DATA_SOURCE_NAME`` may return ``"null"`` for a MySQL ODBC
    datasource, while it returns the actual name of your datasource when you
    retrieve it for an Oracle database. This means that you should
    experiment with the return values a bit, to make sure that you
    understand what values to expect for your specific datasource(s).
