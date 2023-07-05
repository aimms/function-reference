.. aimms:procedure:: OptionGetString(OptionName, CurrentString)

.. _OptionGetString:

OptionGetString
===============

With the procedure :aimms:func:`OptionGetString` you can obtain the string
representation of the current value of an AIMMS option, as displayed in
the AIMMS **Options** dialog box.

.. code-block:: aimms

    OptionGetString(
         OptionName,          ! (input) scalar string expression
         CurrentString        ! (output) scalar string parameter
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *CurrentString*
        A scalar string parameter that, on return, contains the string
        representation of the current value of the option.

Return Value
------------

    The procedure returns 1 if the option exists, or 0 if the name refers to
    a non-existent option.

.. note::

    -  Options for which strings are displayed in the AIMMS **Options** dialog
       box, are represented by numerical (integer) values internally. To obtain
       the numerical option value, or to obtain the mapping between numerical
       option values and the corresponding string keywords, you can use the
       procedures :aimms:func:`OptionGetValue` and :aimms:func:`OptionGetKeywords`.

    -  The procedure :aimms:func:`OptionGetString` can also be used to set
       a solver specific option by prefixing the option name by the name of
       the solver followed by a double colon ``::``, e.g.,
       'CPLEX 22.1::LP method'.

.. seealso::

    :aimms:func:`OptionGetValue`, :aimms:func:`OptionGetKeywords`, :aimms:func:`OptionSetString`.
