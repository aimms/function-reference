.. aimms:procedure:: OptionGetDefaultString(OptionName, DefaultString)

.. _OptionGetDefaultString:

OptionGetDefaultString
======================

With the procedure :aimms:func:`OptionGetDefaultString` you can obtain the string
representation of the current value of an AIMMS option, as displayed in
the AIMMS **Options** dialog box.

.. code-block:: aimms

    OptionGetDefaultString(
         OptionName,          ! (input) scalar string expression
         DefaultString        ! (output) scalar string parameter
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *DefaultString*
        A scalar string parameter that, on return, contains the string
        representation of the default value of the option.

Return Value
------------

    The procedure returns 1 if the option exists, or 0 if the name refers to
    a non-existent option.

.. seealso::

    :aimms:func:`OptionGetValue`, :aimms:func:`OptionGetKeywords`, :aimms:func:`OptionGetString`.
