.. aimms:function:: SQLNumberOfDrivers(DatabaseInterface)

.. _SQLNumberOfDrivers:

SQLNumberOfDrivers
==================

With the function :aimms:func:`SQLNumberOfDrivers` you can determine the number of
installed ODBC drivers on your system.

.. code-block:: aimms

    SQLNumberOfDrivers(
         DatabaseInterface,   ! (input) an element expression
         )

Arguments
---------

    *DatabaseInterface*
        Element value into the set AllDatabaseInterfaces. Currently, this set
        contains only the value ``'ODBC'``.

Return Value
------------

    The function returns the number of installed ODBC drivers on your system
    (using ``'ODBC'`` as argument). In case none are installed, the value
    ``0`` is returned. In case of an error, ``-1`` is returned.

.. note::

    This function should be used in combination with the function :aimms:func:`SQLDriverName`,
    to determine all ODBC drivers installed on your system.

.. seealso::

    The functions :aimms:func:`SQLDriverName` and :aimms:func:`SQLCreateConnectionString`.
