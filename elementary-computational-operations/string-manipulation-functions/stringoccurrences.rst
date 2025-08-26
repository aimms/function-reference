.. aimms:function:: StringOccurrences(SearchString, Key, CaseSensitive, WordOnly, IgnoreWhite)

.. _StringOccurrences:

StringOccurrences
=================

The function :aimms:func:`StringOccurrences` counts the number of occurrences of a
particular substring in a string.

.. code-block:: aimms

    StringOccurrences(
         SearchString,    ! (input) a string expression
         Key,             ! (input) a string expression
         [CaseSensitive], ! (optional) binary
         [WordOnly],      ! (optional) binary
         [IgnoreWhite]    ! (optional) binary
         )

Arguments
---------

    *SearchString*
        A string in which you want to find the substring(s).

    *Key*
        The substring.

    *CaseSensitive*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option
        ``Case_sensitive_string_comparison``, and is 1 if this option is :menuselection:`On`
        and 0 if this option is :menuselection:`Off`. The default of the option
        ``Case_sensitive_string_comparison`` is :menuselection:`On`.

    *WordOnly*
        It is a word only search when this option is set to 1. The default is 0.

    *IgnoreWhite*
        The search ignores whites if this option is set to 1. The default is 0.

Return Value
------------

    The function returns how many occurrences of the substring *Key* exist
    in the string *SearchString*.




Example
-----------

The code:

.. code-block:: aimms

	sp_str := "Hello Hello";
	sp_key := "Hello";
	p_res := StringOccurrences(
		SearchString  :  sp_str, 
		Key           :  sp_key, 
		CaseSensitive :  1, 
		WordOnly      :  0,
		IgnoreWhite   :  0);
	display p_res ; ! p_res := 2 ;


.. seealso::

    - The functions :aimms:func:`FindString`, :aimms:func:`FindNthString`.
