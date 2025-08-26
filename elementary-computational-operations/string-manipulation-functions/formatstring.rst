.. aimms:function:: FormatString(formatstring, arguments,...)

.. _FormatString:

FormatString
============

With the :aimms:func:`FormatString` function you can compose a string that is
built up from combinations of numbers, strings and set elements. The
:aimms:func:`FormatString` function accepts a varying number of arguments, defined
by the conversion specifiers in the format string.

.. code-block:: aimms

    FormatString(
         formatstring,    ! (input) a literal double quoted string
         arguments,       ! (input) a list of numbers, strings, and set elements
         ...
         )

Arguments
---------

    *formatstring*
        A format string that specifies how the returned string is composed. The
        string should contain the proper conversion specifier for each following
        argument.

    *arguments,...*
        One or more arguments of type number, string or element. The order of
        these arguments must coincide with the order of the conversion
        specifiers in *formatstring*.

Return Value
------------

    The function returns the formatted string.


Example
-----------

The code:

.. code-block:: aimms

	p_million := 1e6 ;
	sp_millions := formatString("%i %6.3n %.0g", p_million, p_million, p_million );
	display sp_millions  ; ! sp_millions := "1000000 1.000e+06 1e+06" ;

Is a first illustration of various ways of formatting a number.


.. seealso::

    - For a detailed description of the conversion specifiers in AIMMS see :ref:`sec:set-expr.string.format` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
