.. aimms:function:: Card(Identifier, Suffix)

.. _Card:

Card
====

The function :aimms:func:`Card` returns the cardinality of an identifier, or the
cardinality of a suffix of that identifier. To support the various
usages there are three different flavors of Card:

.. code-block:: aimms

    Card(
        Identifier    ! (input) a set expression
        )

.. code-block:: aimms

    Card(
        Identifier    ! (input) an identifier reference
        )

.. code-block:: aimms

    Card(
        Identifier,    ! (input) element in the set AllIdentifiers
        [Suffix]       ! (optional) element in the set AllSuffixNames
        )

Arguments
---------

    *Identifier*
        A reference to an identifier that may contain data, or a simple set or a
        set expression.

    *Suffix*
        An element in the predefined set of :aimms:set:`AllSuffixNames`.

Return Value
------------

    If the first argument is a set (expression), the function will return
    the number of elements in the set. In all other cases the function
    returns the number of nondefault values stored in the data of the given
    identifier, or in the data of the suffix of that identifier.


Example
-----------

.. code-block:: aimms

	! Some data
	_s_genders := data { male, female };
	_s_names := data { John, Jill, Jack, Joan } ;
	_s_nameByGender(_i_gender) := data {
		male : { John, Jack },
		female : { Jill, Joan } 
	} ;

	! Getting the cardinality of a set
	_p_noGenders := card(_s_genders); ! Returns 2
	_p_noNames := card( _s_names );  ! Returns 4

	! Getting the cardinality of sets in an indexed set
	_p_noNamesByGender(_i_gender) := 
		card( _s_nameByGender( _i_gender ) ); ! Returns 2, twice.


.. note::

    -  The :aimms:func:`Card` function cannot be applied to slices of indexed
       identifiers. In such a case, you can use the ``Count`` operator to
       count the number of nondefault elements.

    -  When the :aimms:func:`Card` function is used inside the definition of a
       parameter or a set and the first argument is an index or element
       parameter into the set :aimms:set:`AllIdentifiers` (using the third prototype above)
       then the definition depends on all identifiers that can appear on the
       left hand side of an assignment (sets without a definition,
       parameters without a definition, variables and constraints). The
       cardinality will be computed for all identifiers, including those
       with a definition. These definitions will not be made up to date,
       however. This is illustrated in the following example. 

       .. code-block:: aimms

                       Parameter A;
                       Parameter B {
                           Definition   :  A + 1;
                       }
                       Parameter TheCards {
                           IndexDomain  :  IndexIdentifiers;
                           Definition   :  Card( IndexIdentifiers, 'Level' );
                       }
                       Body:
                           A := 1;
                           display TheCards;

       Here ``TheCards`` is computed in the display statement because ``A``
       just changed. The definition of ``TheCards``, that is made up to date
       by the display statement, will, however, not invoke the computation
       of ``B``, although it is not up to date. This is done in order to
       avoid circular references while making set and parameter definitions
       up to date. In order to make ``B`` up to date consider using the
       ``Update`` statement, see also :doc:`non-procedural-language-components/execution-of-nonprocedural-components/nonprocedural-execution` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

.. seealso::

    The function :aimms:func:`ActiveCard` and the ``Count`` operator (see also :doc:`non-procedural-language-components/execution-of-nonprocedural-components/nonprocedural-execution`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__).
