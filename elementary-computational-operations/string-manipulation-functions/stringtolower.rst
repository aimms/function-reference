.. aimms:function:: StringToLower(text)

.. _StringToLower:

StringToLower
=============

The function :aimms:func:`StringToLower` converts all characters of a string to
lower case.

.. code-block:: aimms

    StringToLower(
         text            ! (input) a scalar string expression
         )

Arguments
---------

    *text*
        The string that you want to convert to lower case characters.

Return Value
------------

    The function returns the lower case string.


Example
-----------

The code:

.. code-block:: aimms

	sp_str := "hello HELLO";
	sp_res := StringToLower( sp_str );
	display sp_res ; ! sp_res := "hello hello" ;



.. seealso::

    The functions :aimms:func:`StringToUpper`, :aimms:func:`StringCapitalize`.
