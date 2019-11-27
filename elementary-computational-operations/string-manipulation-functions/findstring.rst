.. aimms:function:: FindString(SearchString, Key, CaseSensitive, WordOnly, IgnoreWhite)

.. _FindString:

FindString
==========

The function :aimms:func:`FindString` searches for the occurrence of a substring
(a key) within a search string.

.. code-block:: aimms

    FindString(
         SearchString,    ! (input) a scalar string expression
         Key,             ! (input) a scalar string expression
         [CaseSensitive], ! (optional) binary
         [WordOnly],      ! (optional) binary
         [IgnoreWhite]    ! (optional) binary
         )

Arguments
---------

    *SearchString*
        The string in which you want to find the substring *key*.

    *Key*
        The substring to search for.

    *CaseSensitive*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option
        ``Case_sensitive_string_comparison``, and is 1 if this option is 'On'
        and 0 if this option is 'Off'. The default of the option
        ``Case_sensitive_string_comparison`` is 'On'.

    *WordOnly*
        It is a word only search when this option is set to 1. The default is 0.

    *IgnoreWhite*
        The search ignores whites if this option is set to 1. The default is 0.

.. note::

    As with all string comparisons within AIMMS, the function :aimms:func:`FindString`
    is case sensitive by default. You can modify this behavior through the
    option ``Case_Sensitive_String_Comparison``.

Return Value
------------

    The function returns the start position of the first occurrence of the
    substring. If the substring does not exist, then the function returns 0.

.. seealso::

    The functions :aimms:func:`FindNthString`, :aimms:func:`RegexSearch`.
