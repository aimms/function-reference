.. aimms:function:: ElementRange(from, to[, incr][, prefix][, postfix][, fill])

.. _ElementRange:

ElementRange
============

With the function :aimms:func:`ElementRange` you can create a set with elements in
which each element can be constructed using a prefix string, a postfix
string, and a a sequential number.

.. code-block:: aimms

    ElementRange(
         from,            ! (input) integer expression
         to,              ! (input) integer expression
         [incr,]          ! (optional) integer expression
         [prefix,]        ! (optional) string expression
         [postfix,]       ! (optional) string expression
         [fill]           ! (optional) 0 or 1
         )

Arguments
---------

    *from*
        The integer value for which the first element must be created

    *to*
        The integer value for which the last element must be created

    *incr (optional)*
        The integer-valued interval length between two consecutive elements. If
        omitted, then the default interval length of 1 is used.

    *prefix (optional)*
        The prefix string for every element. If omitted, then the elements have
        no prefix (and thus start with the number).

    *postfix (optional)*
        The postfix string for every element. If omitted, then the elements have
        no postfix (and thus end with the number).

    *fill (optional)*
        This logical indicator specifies whether the numbers must be padded with
        leading zeroes. If omitted, then the default value 1 is used.

Return Value
------------

    The function returns a set containing the created elements.
