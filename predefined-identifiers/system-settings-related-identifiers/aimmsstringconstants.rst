.. aimms:set:: AimmsStringConstants

.. _AimmsStringConstants:

AimmsStringConstants
====================

The predefined string parameter :aimms:set:`AimmsStringConstants` contains the
constituents that determine the running version of AIMMS. It is used to
determine which installation of AIMMS is running.

.. code-block:: aimms

        StringParameter AimmsStringConstants {
            IndexDomain :  ( IndexAimmsStringConstantElements );
        }

    This string parameter contains the following elements:

-  **``Platform``** AIMMS supports the platform ``"Windows"``, and the
   platform ``"Linux"``.

-  **``Architecture``** The architecture for 32 bit systems is known as
   ``"x86"``, and the architecture for 64 bit systems is known as
   ``"x64"``.

-  **``Flavor``** AIMMS comes only in a single flavor: ``"utf8"``. Up to
   AIMMS 3.13, AIMMS came in the single byte per character flavor,
   abbreviated to ``"asc"``, and it came in the two byte per character
   flavor, abbreviated to ``"uni"``. For the ``Linux`` platform only the
   ``asc`` flavor was available.

Example
-------

    .. code-block:: aimms

                StringParameter myDllName {
                    Definition : {
                        AimmsStringConstants('Architecture') + "\" +
                        AimmsStringConstants('Flavor') + "\" +
                        "myDll.dll"
                    }
                }

    A possible outcome of ``myDllName`` is
    ``x86\asc\myDll.dll``.

.. seealso::

    The function :aimms:func:`EnvironmentGetString` and the predeclared set :aimms:set:`AllAimmsStringConstantElements`.
