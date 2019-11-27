.. aimms:function:: Character(n)

.. _Character:

Character
=========

The function :aimms:func:`Character` returns the string consisting of a single
character whose ordinal number is the value of the argument.

.. code-block:: aimms

    Character(
         n            ! (input) a numeric expression
         )

Arguments
---------

    *n*
        A numeric expression in the range
        :math:`\{ 0 .. 55295 \} \cup \{ 57344 .. 65535 \}`.

Return Value
------------

    The function Character returns a string of length 1. Exception: when the
    value 0 is passed it returns the empty string.

.. seealso::

    The function :aimms:func:`CharacterNumber`.
