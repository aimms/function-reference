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

Example
-----------

The code:

.. code-block:: aimms

	_s_ints     := ElementRange(1,12);
	_s_regions  := ElementRange(1,12,prefix:"reg",fill:0);
	_s_products := ElementRange(1,12,prefix:"prd",fill:1);
	display _s_ints, _s_regions, _s_products ;

produces 

.. code-block:: aimms

    _s_ints := data { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 } ;

    _s_regions := data { reg1, reg2, reg3, reg4, reg5, reg6, reg7, reg8, reg9, reg10, reg11, reg12 } ;

    _s_products := data { prd01, prd02, prd03, prd04, prd05, prd06, prd07, prd08, prd09, prd10, prd11, prd12 } ;

in the listing file.