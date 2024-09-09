.. aimms:function:: GetAnnotationValues(AnnotationKey,Values)

.. _GetAnnotationValues:

GetAnnotationValues
=======================

The pocedure :aimms:func:`GetAnnotationValues` collects for all identifiers the annotation value for annotation ``AnnotationKey``.

.. code-block:: aimms

    GetAnnotationValues(
         AnnotationKey,  ! (input)   string expression
		 Values          ! (output)  string parameter indexed over AllIdentifiers
    )

Arguments
---------

    *AnnotationKey*
        A string expression that results in a valid annotation key

    *Values*
        A string parameter that is indexed over :aimms:set:`AllIdentifiers`



Return Value
------------

    This procedure returns 1 upon success.

Example
-------

Given the declaration: 

.. code-block:: aimms

	StringParameter _sp_annot {
		IndexDomain: IndexIdentifiers;
	}


The code:

.. code-block:: aimms

	GetAnnotationValues(
		AnnotationKey :  "aimmsunit::TestSuite", 
		Values        :  _sp_annot);
	display _sp_annot('chapterModel::sectionModelQuery::funcGetAnnotationValues::pr_testGetAnnotationValues');

Produces in the listing file:

.. code-block:: aimms

    _sp_annot('chapterModel::sectionModelQuery::funcGetAnnotationValues::pr_testGetAnnotationValues') := "modelQuery" ;



.. seealso::

    The functions :aimms:func:`DeclaredSubset` and :aimms:func:`DomainIndex`.
