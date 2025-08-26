.. aimms:function:: RegexReplace(SearchString, Pattern, Replacement [, CaseSensitive])

.. _RegexReplace:

RegexReplace
============

The function :aimms:func:`RegexReplace` finds all matches with the given regular expression and replaces them 
with the specified replacement. The modified string is returned.

.. code-block:: aimms

    RegexReplace(
         SearchString,    ! (input) a scalar string expression
         Pattern,         ! (input) a scalar string expression
         Replacement,     ! (input) a scalar string expression
         [CaseSensitive]  ! (optional) binary
         )

Arguments
---------

    *SearchString*
        The string in which you want to find a substring matching the regex
        *pattern*.

    *Pattern*
        The regular expressions pattern to match. Multilines are not supported.

    *Replacement*
        The pattern to use as replacement of each found match.

    *CaseSensitive (optional)*
        The search will be case sensitive when the value is 1. The default
        depends on the setting of the option ``Case_sensitive_string_comparison``, and is 1 if this option is :menuselection:`On`
        and 0 if this option is :menuselection:`Off`. The default of the option ``Case_sensitive_string_comparison`` is :menuselection:`On`.

.. note::

    -  The used regular expressions grammar follows the implementation of
       the `modified ECMAScript regular expression grammar in the C++
       Standard Library <https://en.cppreference.com/w/cpp/regex/ecmascript>`__. It follows `ECMA-262 grammar <https://ecma-international.org/ecma-262/>`__ and `POSIX grammar <http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03>`__,
       with some modifications.

    -  To include a special character in a string, it should be escaped by
       the backslash character ``\`` (for more information on special
       characters see also :ref:`sec:set-expr.string.format`. In
       regular expressions, special characters also have to be escaped in
       order to be included in a pattern. For example, in order to match
       a backslash character the pattern should contain four backslashes
       (see the example below).

Return Value
------------

    The function returns a new string where all replacements are applied. If the pattern was not found
    in the input string the returned strings is the same as the input string.

Example
-------

The following example will replace all vowels with a ``*``

.. code-block:: aimms

    str := RegexReplace("The quick brown fox", "a|e|i|o|u", "*" 0);

results in ``str`` being ``Q**ck br*wn f*x``.

And in the following example all vowels will be replaced by the same vowel in between brackets

.. code-block:: aimms

    str := RegexReplace("The quick brown fox", "a|e|i|o|u", "[$&]" 0);

results in ``str`` being ``Q[u][i]ck br[o]wn f[o]x``.

.. seealso::

    - The functions :aimms:func:`RegexSearch`, :aimms:func:`FindReplaceStrings`.
