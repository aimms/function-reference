.. aimms:function:: ActiveCard(Identifier, Suffix)

.. _ActiveCard:

ActiveCard
==========

The function :aimms:func:`ActiveCard` returns the cardinality of active elements
in its identifier argument, or the cardinality of active elements of a
suffix of that identifier.

.. code-block:: aimms

    ActiveCard(
        Identifier,    ! (input) identifier reference
        [Suffix]       ! (optional) element in the set AllSuffixNames
        )

An element in identifier P is active if its tuple components are within the domain sets of P and 
within the index domain condition of P (if any). Otherwise it is inactive.

Arguments
---------

    *Identifier*
        A reference to a set or an indexed identifier.

    *Suffix*
        An element in the predefined set :aimms:set:`AllSuffixNames`.

Return Value
------------

    #.  If *Identifier* is a set, the function ActiveCard returns the number of 
        active elements in *Identifier*. 
    
    #.  If *Identifier* is an indexed identifier, the function ActiveCard returns the number of active elements
        in *Identifier*. 
    
    #.  If *Suffix* is given, the number of active elements for the given suffix of *Identifier*.

.. note::

    The :aimms:func:`ActiveCard` function cannot be applied to slices of indexed
    identifiers. In such a case, you can use the ``Count`` operator to count
    the number of active elements.



Example
-----------

.. code-block:: aimms

	! Small data set: keeping stock of two fruits.
	_s_fruits := data { apple, pear } ;
	_p_stock(_i_fruit) := data { apple : 4, pear : 5 } ;

	! Removing one fruit from our data set.
	_s_fruits -= data { pear };
	! There is now only one fruit left in _p_stock - _p_stock has one active and one inactive element.

	display _p_stock ; ! Writes "_p_stock(_i_fruit) := data { apple : 4 };" to listing file.

	_p_activeCard := ActiveCard( _p_stock ); ! 1: ActiveCard returns the number of active elements.
	_p_card := Card( _p_stock ); ! 2; Card returns the number of elements, both active and inactive.

	! The difference between Card and ActiveCard is the number of inactive elements.



.. seealso::

	-	The function :aimms:func:`Card` and ``Count`` operator (see also :ref:`sec:expr.num.iter` of
		the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__).

	-	The procedure :aimms:procedure:`RestoreInactiveElements`

	-	The explanation of inactive elements in the Language Reference at :ref:`inactive_data`.

	-	The AIMMS Developer tool Identifier Cardinalities, see :ref:`sec:debug.card`.