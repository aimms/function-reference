.. aimms:function:: FindNthString(SearchString, Key, Nth, CaseSensitive, WordOnly, IgnoreWhite)

.. _FindNthString:

FindNthString
=============

The function :aimms:func:`FindNthString` searches for the :math:`n`-th occurrence
of a substring (a key) within a search string.

.. code-block:: aimms

    FindNthString(
         SearchString,    ! (input) a scalar string expression
         Key,             ! (input) a scalar string expression
         Nth,             ! (input) an integer expession
         [CaseSensitive], ! (optional) binary
         [WordOnly],      ! (optional) binary
         [IgnoreWhite]    ! (optional) binary
         )

Arguments
---------

    *SearchString*
        The string in which you want to find the substring *Key*.

    *Key*
        The substring to search for.

    *Nth*
        The function will search for the *Nth* occurrence of the substring. If
        this number is negative, then the function will search backwards
        starting from the right.

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

    As with all string comparisons within AIMMS, the function
    :aimms:func:`FindNthString` is case sensitive by default. You can modify this
    behavior through the option ``Case_Sensitive_String_Comparison``.

Return Value
------------

    The function returns the start position of the :math:`n`-th occurrence
    of the substring starting from the left (or right). If the substring
    does not exist within the string, or does not occur *Nth* times then the
    function returns 0. When the argument ``Nth`` is 0, then this function
    will always return 0.

.. seealso::

    The functions :aimms:func:`FindString`, :aimms:func:`StringOccurrences`, :aimms:func:`RegexSearch`.
