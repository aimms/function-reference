.. aimms:function:: RegexSearch(SearchString, Pattern[, CaseSensitive])

.. _RegexSearch:

RegexSearch
===========

The function :aimms:func:`RegexSearch` tells if there is a substring in the search
string that matches the regex pattern.

.. code-block:: aimms

    RegexSearch(
         SearchString,    ! (input) a scalar string expression
         Pattern,         ! (input) a scalar string expression
         [CaseSensitive]  ! (optional) binary
         )

Arguments
---------

    *SearchString*
        The string in which you want to find a substring matching the regex
        *pattern*.

    *Pattern*
        The regular expressions pattern to match. Multilines are not supported.

    *CaseSensitive (optional)*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option ``Case_sensitive_string_comparison``, and is 1 if this option is 'On'
        and 0 if this option is 'Off'. The default of the option ``Case_sensitive_string_comparison`` is 'On'.

.. note::

    -  The used regular expressions grammar follows the implementation of
       the `modified ECMAScript regular expression grammar in the C++
       Standard Library <https://en.cppreference.com/w/cpp/regex/ecmascript>`__. It follows `ECMA-262 grammar <https://ecma-international.org/ecma-262/>`__ and `POSIX grammar <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03>`__,
       with some modifications.

    -  To include a special character in a string, it should be escaped by
       the backslash character ``\`` (for more information on special
       characters see also :ref:`sec:set-expr.string.format` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__). In
       regular expressions special characters also have to be escaped in
       order to be included in a pattern. So, for example, in order to match
       a backslash character the pattern should contain four backslashes
       (see the example below).

Return Value
------------

    The function returns 1 if a substring that matches the regex pattern
    exists in the search string. When the pattern is an empty string, the
    function returns 1. In all other cases, the function returns 0.

Example
-------

    The following example checks if the path contains the specified folder
    name on disk C. With the following declarations (and initial data):

    .. code-block:: aimms

                Parameter P;
                StringParameter path {
                    InitialData: "C:\\ProgramFiles\\Folder\\SubFolder";
                }
                StringParameter regexPattern {
                    InitialData: "c:.*\\\\ProgramFiles(\\\\|$)";
                }

    the statement 

    .. code-block:: aimms

                P := regexsearch(path, regexPattern, 0);

    results in ``P`` being 1.
	
    The used regular expression pattern specifies that the path starts
    with ``c:``, followed by zero or more characters (regular expression: ``.*``), followed by ``\ProgramFiles`` (regular expression: ``\\\\ProgramFiles``), and ends with a backslash or the end of a line
    (regular expression: ``(\\\\|$)``).

.. seealso::

    The functions :aimms:func:`FindString`, :aimms:func:`FindNthString`.
