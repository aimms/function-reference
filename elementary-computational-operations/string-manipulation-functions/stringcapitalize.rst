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

.. seealso::

    The functions :aimms:func:`StringToLower`, :aimms:func:`StringToUpper`.
