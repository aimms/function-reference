.. aimms:procedure:: OptionGetKeywords(OptionName, Keywords)

.. _OptionGetKeywords:

OptionGetKeywords
=================

With the procedure :aimms:func:`OptionGetKeywords` you can obtain set of string
keywords, as displayed in the AIMMS **Options** dialog box, that
correspond to the numerical (integer) values of an option.

.. code-block:: aimms

    OptionGetKeywords(
         OptionName,          ! (input) scalar string expression
         Keywords             ! (output) a 1-dimensional string parameter
         )

Arguments
---------

    *OptionName*
        A string expression holding the name of the option.

    *Keywords*
        A 1-dimensional string parameter that, on return, contains the keywords
        corresponding to the set of possible (integer) option values.

Return Value
------------

    The procedure returns 1 if the option exists, and 0 if the *OptionName*
    refers to a non-existent option or if the domain set of the
    1-dimensional string parameter is too small.

.. note::

    The domain set of the 1-dimensional parameter passed as the *Keywords*
    argument must have sufficient elements to hold the string keywords of
    the (integer) option values from the lower bound up to and including the
    upper bound.

.. seealso::

    :aimms:func:`OptionGetValue`, :aimms:func:`OptionGetString`, :aimms:func:`OptionSetString`.
