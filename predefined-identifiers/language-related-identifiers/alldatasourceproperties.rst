.. aimms:set:: AllDataSourceProperties

.. _AllDataSourceProperties:

AllDataSourceProperties
=======================

The predefined set :aimms:set:`AllDataSourceProperties` contains all datasource
properties, which can be queried using the function
``GetDataSourceProperty``.

.. code-block:: aimms

        Set AllDataSourceProperties {
            Index      :  IndexDataSourceProperties;
            Definition :  
                 data { SQL_DATA_SOURCE_NAME, SQL_DATA_SOURCE_READ_ONLY,
                        SQL_DBMS_NAME, SQL_DBMS_VER, SQL_DRIVER_NAME,
                        SQL_DM_VER, SQL_DRIVER_VER, SQL_KEYWORDS,
                        SQL_SERVER_NAME }
            }
        }

Definition
----------

    The set :aimms:set:`AllDataSourceProperties` contains all datasource properties,
    which can be queried using the function ``GetDataSourceProperty``. They
    are:

    -  ``SQL_DATA_SOURCE_NAME`` : The name of the datasource.

    -  ``SQL_DATA_SOURCE_READ_ONLY`` : The read-only status of the
       datasource. Returns ``"Yes"`` or ``"No"``.

    -  ``SQL_DBMS_NAME`` : The name of the database system (e.g., returns
       ``"Oracle"`` for an Oracle database).

    -  ``SQL_DBMS_VER`` : The version of the database system.

    -  ``SQL_DRIVER_NAME`` : The actual DLL of the ODBC driver for the
       datasource.

    -  ``SQL_DM_VER`` : The version of the ODBC driver manager.

    -  ``SQL_DRIVER_VER`` : The version of the ODBC driver for the
       datasource.

    -  ``SQL_KEYWORDS`` : A comma-separated list of all reserved keywords of
       the datasource.

    -  ``SQL_SERVER_NAME`` : The datasource-specific server name.

Updatability
------------

    The contents of the set cannot be modified.

.. seealso::

    The function :aimms:func:`GetDataSourceProperty`.
