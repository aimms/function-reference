.. aimms:procedure:: OptionGetValue(OptionName, Lower, current, Default, Upper)

.. _OptionGetValue:

OptionGetValue
==============

With the procedure :aimms:func:`OptionGetValue` you can obtain the current value
of an AIMMS option, as well as its lower and upper bound and default
value.

.. code-block:: aimms

    OptionGetValue(
         OptionName,          ! (input) scalar string expression
         Lower,               ! (output) scalar numerical parameter
         Current,             ! (output) scalar numerical parameter
         Default,             ! (output) scalar numerical parameter
         Upper                ! (output) scalar numerical parameter
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *Lower*
        A scalar parameter that, on return, contains the lower bound of the
        possible option values.

    *current*
        A scalar parameter that, on return, contains the current (numerical)
        value of the option.

    *Default*
        A scalar parameter that, on return, contains the default (numerical)
        value of the option.

    *Upper*
        A scalar parameter that, on return, contains the upper bound of the
        possible option values.

Return Value
------------

    The procedure returns 1 if the option exists, or 0 if the name refers to
    a non-existent option or to an option that does not take a number as
    value.

.. note::

    -  Options for which strings are displayed in the AIMMS **Options**
       dialog box, are also represented by numerical (integer) values. To
       obtain the corresponding option keywords, you can use the procedures
       :aimms:func:`OptionGetString` and :aimms:func:`OptionGetKeywords`.

    -  You can modify option values programmatically using the ``OPTION``
       statement (see also :doc:`procedural-language-components/execution-statements/the-option-and-property-statements` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__), or using
       the procedures :aimms:func:`OptionSetValue` and :aimms:func:`OptionSetString`.

.. seealso::

    :aimms:func:`OptionGetString`, :aimms:func:`OptionGetKeywords`, :aimms:func:`OptionSetValue`, :aimms:func:`OptionSetString`.
