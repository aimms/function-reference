.. aimms:function:: StringCapitalize(text)

.. _StringCapitalize:

StringCapitalize
================

The function :aimms:func:`StringCapitalize` converts the first character of a
string to upper case, and all other characters to lower case.

.. code-block:: aimms

    StringCapitalize(
         text            ! (input) a scalar string expression
         )

Arguments
---------

    *text*
        The string that you want to capitalize.

Return Value
------------

    The function returns the capitalized string.


Example
-----------

The code:

.. code-block:: aimms

	sp_str := "hello HELLO";
	sp_res := StringCapitalize( sp_str );
	display sp_res ; ! sp_res := "Hello hello" ;



.. seealso::

    The functions :aimms:func:`StringToLower`, :aimms:func:`StringToUpper`.
