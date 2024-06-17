.. aimms:function:: StringLength(text)

.. _StringLength:

StringLength
============

The function :aimms:func:`StringLength` returns the number of characters in a
string.

.. code-block:: aimms

    StringLength(
         text            ! (input) a scalar string expression
         )

Arguments
---------

    *text*
        The string for which you want to retrieve the length.

Return Value
------------

    The function returns the number of characters in the string.

Example
-----------

.. code-block:: aimms

	sp_str := "hello HELLO";
	p_res := StringLength( sp_str );
	display p_res ; ! p_res := 11 ;
