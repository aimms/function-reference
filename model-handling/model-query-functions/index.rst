.. _chap:model.query.functions:

Model Query Functions
---------------------

AIMMS supports the following functions to query the structure of the
identifiers in the model:

.. toctree::
   :maxdepth: 1

   attributetostring
   attributelength
   attributecontainsstring
   callerattribute
   callerline
   callernode
   callernumberoflocations
   constraintvariables
   declaredsubset
   domainindex
   identifierattributes
   identifierdimension
   identifiershowattributes
   identifierelementrange
   identifiershowtreelocation
   identifiertext
   identifiertype
   identifierunit
   indexrange
   isruntimeidentifier
   referencedidentifiers
   sectionidentifiers
   variableconstraints

.. code-block:: aimms
   :caption: A common model query example
   :name: CommonModelQueryExample
   
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