.. aimms:function:: StringToUpper(text)

.. _StringToUpper:

StringToUpper
=============

The function :aimms:func:`StringToUpper` converts all characters of a string to
upper case.

.. code-block:: aimms

    StringToUpper(
         text            ! (input) a scalar string expression
         )

Arguments
---------

    *text*
        The string that you want to convert to upper case characters.

Return Value
------------

    The function returns the upper case string.

Example
-----------

The code:

.. code-block:: aimms

	sp_str := "hello HELLO";
	sp_res := StringToUpper( sp_str );
	display sp_res ; ! sp_res := "HELLO HELLO" ;


.. seealso::

    The functions :aimms:func:`StringToLower`, :aimms:func:`StringCapitalize`.
