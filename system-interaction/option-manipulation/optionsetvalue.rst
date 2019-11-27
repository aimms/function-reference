.. aimms:procedure:: OptionSetValue(OptionName, NewValue)

.. _OptionSetValue:

OptionSetValue
==============

With the procedure :aimms:func:`OptionSetValue` you can set the value of a numeric
AIMMS option. The value assigned to the option must be contained in the
option range displayed in the AIMMS **Options** dialog box.

.. code-block:: aimms

    OptionSetValue(
         OptionName,          ! (input) scalar string expression
         NewValue             ! (input) scalar numeric expression
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *NewValue*
        A scalar numeric expression representing the new value to be assigned to
        the option.

Return Value
------------

    The procedure returns 1 if the option exists and the value can be
    assigned to the option, or 0 otherwise.

.. note::

    -  Options for which strings are displayed in the AIMMS **Options**
       dialog box, are also represented by numerical (integer) values. To
       obtain the corresponding option keywords, you can use the procedures
       :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.

    -  You can also modify option values using the ``OPTION`` statement (see
       also Section 8.5 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__).

.. seealso::

    :aimms:func:`OptionGetString`, :aimms:func:`OptionGetKeywords`, :aimms:func:`OptionSetString`.
