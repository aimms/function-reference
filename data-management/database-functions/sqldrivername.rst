.. aimms:function:: SQLDriverName(DatabaseInterface, DriverNo)

.. _SQLDriverName:

SQLDriverName
=============

With the function :aimms:func:`SQLDriverName` you can determine the name of a
certain ODBC driver on your system. This function is designed to be used
in conjunction with the :aimms:func:`SQLNumberOfDrivers` function.

.. code-block:: aimms

    SQLDriverName(
         DatabaseInterface,   ! (input) an element expression
         DriverNo,            ! (input) an integer expression
         )

Arguments
---------

    *DatabaseInterface*
        Element value into the set AllDatabaseInterfaces. Currently, this set
        contains only the value 'ODBC'.

    *DriverNo*
        An integer containing the number of the ODBC driver for which you want
        to retrieve the name. To determine the maximum value of this argument,
        please use the function :aimms:func:`SQLNumberOfDrivers` prior to calling this function. The
        minimum value of this argument is 1.

Return Value
------------

    The function returns the name of the ODBC driver (specified by the
    ``DatabaseInterface`` argument), with the number as specified through
    the ``DriverNo`` argument. If you specify a number outside of the
    correct range, AIMMS will display an error message.

.. note::

    Typically, this function can best be used in a construction like the
    following: 

    .. code-block:: aimms

            NumberOfDrivers := SQLNumberOfDrivers('ODBC');

            while LoopCount <= NumberOfDrivers do
                DriverName := SQLDriverName('ODBC', LoopCount);
                ! Do something with the retrieved table name here...
            endwhile;

    The retrieved name of an ODBC driver, can be used
    as argument in the function :aimms:func:`SQLCreateConnectionString`.

.. seealso::

    - The functions :aimms:func:`SQLNumberOfDrivers` and :aimms:func:`SQLCreateConnectionString`.
