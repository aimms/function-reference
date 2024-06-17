.. aimms:procedure:: SetElementRename(Setname, Element, Newname)

.. _SetElementRename:

SetElementRename
================

With the procedure :aimms:procedure:`SetElementRename` you can rename an element in a
set.

.. code-block:: aimms

    SetElementRename(
         Setname,        ! (input) a set
         Element,        ! (input) an element parameter
         Newname         ! (input) a scalar string expression
         )

Arguments
---------

    *Setname*
        The root set or subset in which you want to rename an element.

    *Element*
        The element that you want to rename.

    *Newname*
        A string holding the new name of the element.

.. note::

    -  If the new name for the element already exists in the set, the
       procedure will generate an execution error.

    -  AIMMS will refuse to rename a set element, if an explicit reference
       to such an element exists in the model source.


Example
-----------

Given the declarations:

.. code-block:: aimms


	Set s_products {
		Index: i_prod;
	}
	Parameter p_rev {
		IndexDomain: i_prod;
	}
	ElementParameter ep_prod {
		Range: s_products;
	}

And a bit of data:

.. code-block:: aimms

	setElementAdd( s_products, ep_prod, "p0" );
	p_rev( ep_prod ) := 1 ;
	display p_rev ; ! p_rev := data { p0 : 1 } ;


The statement

.. code-block:: aimms

	SetElementRename(
		Setname :  s_products, 
		Element :  ep_prod, 
		Newname :  "p1"); 

renames ``p0`` to ``p1``, which can be seen when displaying p_rev again.

.. code-block:: aimms

	display p_rev  ; ! p_rev := data { p1 : 1 } ;



.. seealso::

    -  The procedure :aimms:procedure:`SetElementAdd`, and the function :aimms:func:`StringToElement`.

    -  The lexical conventions for set elements in :doc:`preliminaries/language-preliminaries/lexical-conventions`.
