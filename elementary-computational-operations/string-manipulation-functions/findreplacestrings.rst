.. aimms:function:: FindReplaceStrings(SearchString, Key, Replacement, CaseSensitive, WordOnly)

.. _FindReplaceStrings:

FindReplaceStrings
==================

The function :aimms:func:`FindReplaceStrings` constructs a string by searching for
every occurrence of a substring (a key) within a search string and
replaces it with another string. It returns the constructed string.

.. code-block:: aimms

    FindReplaceStrings(
         SearchString,    ! (input) a scalar string expression
         Key,             ! (input) a scalar string expression
         Replacement,     ! (input) a scalar string expression
         [CaseSensitive], ! (optional) binary
         [WordOnly]       ! (optional) binary
         )

Arguments
---------

    *SearchString*
        The string in which you want to find the substring *key*.

    *Key*
        The substring to search for.

    *Replacement*
        The string used to replace *Key*.

    *CaseSensitive*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option
        ``Case_sensitive_string_comparison``, and is 1 if this option is 'On'
        and 0 if this option is 'Off'. The default of the option
        ``Case_sensitive_string_comparison`` is 'On'.

    *WordOnly*
        It is a word only search when this option is set to 1. The default is 0.

.. note::

    As with all string comparisons within AIMMS, the function
    :aimms:func:`FindReplaceStrings` is case sensitive by default. You can modify this
    behavior through the option ``Case_Sensitive_String_Comparison``.

Return Value
------------

    The function returns the resulting string. If *Key* is not found, the
    original string is returned.

.. seealso::

    The functions :aimms:func:`FindString`, :aimms:func:`StringOccurrences` and :aimms:func:`FindReplaceNthString`.
