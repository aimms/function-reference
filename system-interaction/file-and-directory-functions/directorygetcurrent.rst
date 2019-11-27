.. aimms:procedure:: DirectoryGetCurrent(directory)

.. _DirectoryGetCurrent:

DirectoryGetCurrent
===================

The procedure :aimms:func:`DirectoryGetCurrent` retrieves the full path of the
current project directory.

.. code-block:: aimms

    DirectoryGetCurrent(
            directoryname      ! (output) scalar string parameter
            )

Arguments
---------

    *directory*
        A scalar string parameter, that on return will contain the path of the
        current project directory. The string is always terminated by a
        directory slash :math:`\backslash`.

Return Value
------------

    The procedure returns 1.

.. seealso::

    The procedure :aimms:func:`DirectorySelect`.
