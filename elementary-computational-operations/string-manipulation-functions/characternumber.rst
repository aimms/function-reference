.. aimms:function:: CharacterNumber(text)

.. _CharacterNumber:

CharacterNumber
===============

The function :aimms:func:`CharacterNumber` returns the character number of the
first character in a string. It returns 0 for the empty string.

.. code-block:: aimms

    CharacterNumber(
         text            ! (input) a scalar string expression
         )

Arguments
---------

    *text*
        The string for which you want to have the value of the first character.

Return Value
------------

    The function CharacterNumber returns a value in the range { 0 .. 65535
    }.

.. seealso::

    The function :aimms:func:`Character`.
