.. aimms:set:: CurrentFile

.. _CurrentFile:

CurrentFile
===========

The predefined element parameter :aimms:set:`CurrentFile` contains the name of
the file identifier to which output is currently directed.

.. code-block:: aimms

        ElementParameter CurrentFile {
            Range        :  AllFiles;
        }

Definition
----------

    The element parameter :aimms:set:`CurrentFile` contains the name of the file
    identifier to which output from the ``PUT`` and ``DISPLAY`` statements
    is currently directed.

Updatability
------------

    The value of :aimms:set:`CurrentFile` can be modified both programmatically from
    within the AIMMS model and from within the end-user interface. As a
    result, the output from subsequent ``PUT`` and ``DISPLAY`` statements
    will be redirected to the newly specified file identifier.

.. note::

    Output redirection can equivalently be accomplished using the ``PUT``
    statement. The name of the physical file or window associated with a
    file identifier can be retrieved through the string parameter :aimms:set:`CurrentFileName`.

.. seealso::

    The string parameter :aimms:set:`CurrentFileName`. The ``PUT`` statement is discussed in
    Section 31.2 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__, the ``DISPLAY`` statement in
    Section 31.3.
