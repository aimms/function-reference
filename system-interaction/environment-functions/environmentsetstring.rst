.. aimms:function:: EnvironmentSetString(Key, Value)

.. _EnvironmentSetString:

EnvironmentSetString
====================

With the function :aimms:func:`EnvironmentSetString` you can set environment
variables.

.. code-block:: aimms

    EnvironmentSetString(
         Key,          ! (input) scalar string expression
         Value         ! (input) scalar string parameter
         )

Arguments
---------

    *Key*
        A string expression holding the name of the environment variable.

    *Value*
        A scalar string parameter that contains the string representation of the
        value of you want to assign to the environment variable.

Return Value
------------

    The function returns 1 upon success, or 0 otherwise.

.. note::

    -  With :aimms:func:`EnvironmentSetString` you can change the value for existing
       environment variables as well as create new environment variables.

    -  Note that the function :aimms:func:`EnvironmentSetString` will only change the
       values of variables in the environment associated with the AIMMS
       process.

.. seealso::

    :aimms:func:`EnvironmentGetString`.
