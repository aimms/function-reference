.. aimms:procedure:: OptionSetString(OptionName, NewString)

.. _OptionSetString:

OptionSetString
===============

With the procedure :aimms:func:`OptionSetString` you can set the value of a
string-valued AIMMS option. You must use the values as displayed in the
AIMMS **Options** dialog box.

.. code-block:: aimms

    OptionSetString(
         OptionName,     ! (input) scalar string expressionN
         NewString       ! (input) scalar string expression
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *NewString*
        A scalar string expression representing the string representation of the
        value to be assigned to the option.

Return Value
------------

    The procedure returns 1 if the value can be assigned to the option, or 0
    if the name refers to a non-existent option, or the value to a
    non-existent option value.

.. note::

    -  Options for which strings are displayed in the AIMMS **Options** dialog
       box, are represented by numerical (integer) values internally. To obtain
       the numerical option value, or to obtain the mapping between numerical
       option values and the corresponding string keywords, you can use the
       procedures :aimms:func:`OptionGetValue` and :aimms:func:`OptionGetKeywords`.
    
    -  The procedure :aimms:func:`OptionSetString` can also be used to set
       a solver specific option by prefixing the option name by the name of
       the solver followed by a double colon ``::``, e.g.,
       "CPLEX 22.1::LP method".

.. seealso::

    :aimms:func:`OptionSetValue`, :aimms:func:`OptionGetValue`, :aimms:func:`OptionGetKeywords`.
