.. aimms:function:: FindReplaceNthString(SearchString, Key, Replacement, Nth, CaseSensitive, WordOnly)

.. _FindReplaceNthString:

FindReplaceNthString
====================

The function :aimms:func:`FindReplaceNthString` constructs a string by searching
for the Nth occurrence of a substring (a key) within a search string and
replacing this occurrence with another string. It returns the
constructed string.

.. code-block:: aimms

    FindReplaceNthString(
         SearchString,    ! (input) a scalar string expression
         Key,             ! (input) a scalar string expression
         Replacement,     ! (input) a scalar string expression
         Nth,             ! (input) an integer expession
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

    *Nth*
        The function will search for the *Nth* occurrence of the substring. If
        this number is negative, then the function will search backwards
        starting from the right.

    *CaseSensitive*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option
        ``Case_sensitive_string_comparison``, and is 1 if this option is :menuselection:`On`
        and 0 if this option is :menuselection:`Off`. The default of the option
        ``Case_sensitive_string_comparison`` is :menuselection:`On`.

    *WordOnly*
        It is a word only search when this option is set to 1. The default is 0.

.. note::

    As with all string comparisons within AIMMS, the function
    :aimms:func:`FindReplaceNthString` is case sensitive by default. You can modify
    this behavior through the option ``Case_Sensitive_String_Comparison``.

Return Value
------------

    The function returns the resulting string. If the *Nth* occurrence of
    *Key* is not found, the original string is returned.


Example
-----------

Given the declarations

.. code-block:: aimms

	StringParameter sp_str;
	StringParameter sp_key;
	StringParameter sp_rep;
	StringParameter sp_res;


and a bit of data...

.. code-block:: aimms


	sp_str := "Hello Hello";
	sp_key := "Hello";
	sp_rep := "mr";

The code:

.. code-block:: aimms

	sp_res := FindReplaceNthString(
		SearchString  :  sp_str, 
		Key           :  sp_key, 
		Replacement   :  sp_rep, 
		Nth           :  2, 
		CaseSensitive :  1, 
		WordOnly      :  0);
	display sp_res  ;

will produce the following in the listing file:

.. code-block:: aimms

    sp_res := "Hello mr" ;
 
indicating that the second ``Hello`` is replaced by the string ``mr``.

.. seealso::

    - The functions :aimms:func:`FindNthString`, :aimms:func:`StringOccurrences` and :aimms:func:`FindReplaceStrings`.
