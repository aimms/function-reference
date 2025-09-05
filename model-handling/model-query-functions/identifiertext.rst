.. aimms:function:: IdentifierText(identifierName)

.. _IdentifierText:

IdentifierText
==============

The function :aimms:func:`IdentifierText` returns the string representation of the text attribute of ``identifierName``
or, if the text is not specified, the name of the identifier.

.. code-block:: aimms

    IdentifierText(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the text should be obtained.

Return Value
------------

    This function returns a string containing the text attribute of ``identifierName``.
    If ``identifierName`` is not an identifier, an error message is issued. 
    When the text is not specified, the name of the identifier is returned.

    .. note::

        This function replaces the deprecated suffix :ref:`.txt`.


Example
-------

Given the declaration: 

.. code-block:: aimms

    Parameter p_d {
        Text: "a scalar";
    }

the code:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

    _ep_p := StringToElement(AllIdentifiers, 
        "chapterModel::sectionModelQuery::funcIdentifierText::p_d", 
        create: 0);
    _sp_txt := IdentifierText( _ep_p );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _sp_txt ;
    endblock ;

produces in the listing file:

.. code-block:: aimms

    _sp_txt := "a scalar" ;


.. seealso::

    -  The functions :aimms:func:`IdentifierText`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.