.. aimms:procedure:: SessionArgument(argno, argument)

.. _SessionArgument:

SessionArgument
===============

With the procedure :aimms:func:`SessionArgument` you can retrieve the string value
of any user defined command line argument, that was specified during
startup of AIMMS.

.. code-block:: aimms

    SessionArgument(
         argno,             ! (input) integer number
         argument           ! (output) string valued parameter
         )

Arguments
---------

    *argno*
        An integer greater or equal to 1, representing the argument that you
        want retrieve. If the argument does not exist, then the procedure
        returns 0.

    *argument*
        A string valued parameter, to hold the string of the requested command
        line argument.

Return Value
------------

    The procedure returns 1 on success, and 0 if the request argument number
    does not exist.

.. note::

    When you open an AIMMS project from the command line, AIMMS allows you
    to add an arbitrary number of additional arguments directly after the
    project name. The procedure :aimms:func:`SessionArgument` gives you access to
    these arguments. You can use these arguments, for instance, to specify a
    varying data source name from which you want to read data into your
    model, or run your project in different modes.
