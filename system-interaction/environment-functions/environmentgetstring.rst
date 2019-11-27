.. aimms:procedure:: EnvironmentGetString(Key, Value)

.. _EnvironmentGetString:

EnvironmentGetString
====================

With the procedure :aimms:func:`EnvironmentGetString` you can obtain the string
representation of an environment setting, either set by the process
calling AIMMS or by AIMMS itself.

.. code-block:: aimms

    EnvironmentGetString(
         Key,          ! (input) scalar string expression
         Value         ! (output) scalar string parameter
         )

Arguments
---------

    *Key*
        A string expression holding the name of the environment variable.

    *Value*
        A scalar string parameter that, on return, contains the string
        representation of the current value of the environment variable.

Return Value
------------

    The procedure returns 1 if the variable ``Key`` is available, and 0
    otherwise.

.. note::

    -  The environment variables defined by AIMMS itself are: ``AIMMSROOT``,
       ``AIMMSBIN``, ``AIMMSSOLVERS``, ``AIMMSCFG``, ``AIMMSHELP``,
       ``AIMMSDOC``, ``AIMMSUSERDLL``, ``AIMMSLOG``, ``AIMMSPROJECT``,
       ``AIMMSMODULES``, and ``AIMMSTUTORIAL``.

    -  Examples of environment variables available on a Windows system are
       ``COMPUTERNAME``, ``OS``, ``PATH``, ``TEMP``, ``TMP``, and
       ``USERNAME``. Entering the MSDOS command ``set`` on an MSDOS prompt
       will present you with the set of available environment variables on a
       Windows system. Via the control panel tool ``system`` and then going
       to ``Advanced system settings`` - ``Advanced`` tab -
       ``Environment variables`` button, you can manipulate the set of
       environment variables.

    -  On Linux systems a distinction is made between the variables kept to
       a process itself, and those exported to the environment of all its
       child processes. In a bash shell you can obtain the collection of
       variables set via the bash ``set`` command, and the subset of all
       exported environment variables via the bash ``env`` command. In order
       to make a variable available to the environment, you will have to
       explicitly place it in the environment, via an ``export`` command. In
       several system wide bash scripts, ``/etc/bashrc``, or user startup
       bash scripts, ``~/.bashrc``, export commands such as: 

       .. code-block:: aimms

                 export HOSTNAME
                 export OSTYPE

       can
       be found in order to make these useful environment variables
       available to all processes executed.

.. seealso::

    :aimms:func:`EnvironmentSetString`.
