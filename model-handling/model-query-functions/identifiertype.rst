.. aimms:function:: IdentifierType(identifierName)

.. _IdentifierType:

IdentifierType
==============

The function :aimms:func:`IdentifierType` returns the type of ``identifierName``
as an element in :aimms:set:`AllIdentifierTypes`.

.. code-block:: aimms

    IdentifierType(
         identifierName)       ! (input) scalar element parameter

Arguments
---------

    *identifierName*
        An element expression in the predefined set :aimms:set:`AllIdentifiers` specifying the
        identifier for which the type should be obtained.

Return Value
------------

    This function returns a type as an element in :aimms:set:`AllIdentifierTypes`. If
    ``identifierName`` is not an identifier, an error message is issued.

    .. note::

        This function replaces the suffix :ref:`.type`; this suffix is deprecated.


Example
-------

Given the declaration: 

.. code-block:: aimms

    Parameter p_d  ;

the code:

.. code-block:: aimms
    :linenos:
    :emphasize-lines: 4

    _ep_p := StringToElement(AllIdentifiers, 
        "chapterModel::sectionModelQuery::funcIdentifierType::p_d", 
        create: 0);
    _ep_type := IdentifierType( _ep_p );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _ep_type ;
    endblock ;

produces in the listing file:

.. code-block:: aimms

    _ep_type := 'parameter' ;

And below, a common model query example:

.. code-block:: aimms

    SelectedIdentifiers := AllParameters ; ! Or some other selection.
    
    put outf ;
    
    outf.pagewidth := 255 ; ! Wide
    put "type":20, "  ", "name":32, "  ", "dim  ", "unit":20, "  ", 
    	 "range":20, "  ", "Text", / ;
    put "-"*20,    "  ", "-"*32,    "  ", "---  ", "-"*20,    "  ", "-"*40, / ;
    
    for ( si ) do                                ! For each selected identifier
    	put IdentifierType( si ):20, "  "              ! Type
    		si:32, "  ",                               ! name
    		"(", IdentifierDimension( si ):1:0, ")  ", ! dimension
    		IdentifierUnit( si ):20, "  ",             ! unit
    		IdentifierElementRange( si ):20, "  ",     ! range
    		IdentifierText( si ), /                    ! Documenting text.
    endfor ;
    
    putclose ;

.. seealso::

    -  The functions :aimms:func:`IdentifierDimension` and :aimms:func:`IdentifierUnit`.

    -  :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
