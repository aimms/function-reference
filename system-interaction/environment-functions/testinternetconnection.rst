.. aimms:procedure:: TestInternetConnection(url)

.. _TestInternetConnection:

TestInternetConnection
======================

With the procedure :aimms:func:`TestInternetConnection` you can verify whether an
internet connection to a given URL is possible.

.. code-block:: aimms

    TestInternetConnection(
         url                  ! (input) scalar string expression
         )

Arguments
---------

    *url*
        A string representing the address of the internet site AIMMS will try to
        reach.

Return Value
------------

    The procedure returns 1 on success, and 0 if AIMMS could not establish a
    connection to the specified address (by pinging). On failure, the
    pre-defined identifier :aimms:set:`CurrentErrorMessage` will contain a proper error message.

.. note::

    This procedure will only check whether the host as specified in the url
    can be reached, not whether a certain service is running nor whether a
    certain internet page exists.
