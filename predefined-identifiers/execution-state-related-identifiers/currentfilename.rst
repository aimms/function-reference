.. aimms:set:: CurrentFileName

.. _CurrentFileName:

CurrentFileName
===============

The predefined string parameter :aimms:set:`CurrentFileName` contains the file
name associated with the file identifier to which output is currently
directed.

.. code-block:: aimms

        StringParamter CurrentFileName;

Definition
----------

    The string parameter :aimms:set:`CurrentFileName` contains the file name
    associated with the file identifier (as specified in its ``Name``
    attribute) to which output from the ``PUT`` and ``DISPLAY`` statements
    is currently directed.

Updatability
------------

    The value of :aimms:set:`CurrentFileName` is only for display purposes. It can be
    modified programmatically from within the AIMMS model, but the output
    from ``PUT`` and ``DISPLAY`` will always be sent to the file or window
    whose name is specified in the ``Name`` attribute of the corresponding
    file identifier.

.. note::

    The physical file name associated with a file identifier can be changed
    dynamically, by entering a string parameter in the ``Name`` attribute of
    the file identifier. The file identifier to which output is currently
    directed can be retrieved through the element parameter :aimms:set:`CurrentFile`.

.. seealso::

    The element parameter :aimms:set:`CurrentFile`. File identifiers are discussed in
    Section 31.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
