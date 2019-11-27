.. aimms:function:: SubString(str, from, to)

.. _SubString:

SubString
=========

The function :aimms:func:`SubString` retrieves a substring from a specific string,
based on the start and end position of this substring within this
string.

.. code-block:: aimms

    SubString(
         str,      ! (input) a scalar string expression
         from,     ! (input) an integer value
         to        ! (input) an integer value
         )

Arguments
---------

    *str*
        The string from which you want to retrieve the substring.

    *from*
        The start position of the substring within *str*.

    *to*
        The end position of the substring within *str*.

Return Value
------------

    The function returns the requested substring.

.. note::

    If the arguments *from* and *to* are positive, then the position is
    calculated from the start of the string (i.e. the first character is on
    position \ :math:`1`). If the arguments *from* and *to* are negative,
    then the position is calculated from the end of the string (i.e. the
    last character is on position \ :math:`-1`). *from* must be less than or
    equal to *to*, and if either of the values exceeds the length of the
    string, they are automatically set within the proper range.
