.. aimms:function:: ScalarValue(identifier, suffix)

.. _ScalarValue:

ScalarValue
===========

.. code-block:: aimms

    ScalarValue(
        identifier,   ! (input) element expression into AllIdentifiers
        suffix        ! (optional) element expression into AllSuffixNames
       )

Arguments
---------

    *identifier*
        A scalar element expression into :aimms:set:`AllIdentifiers`.

    *suffix*
        A scalar element expression into :aimms:set:`AllSuffixNames`.

Return Value
------------

    The function :aimms:func:`ScalarValue` returns the value contained in the scalar
    identifier *identifier* or scalar reference *identifier.suffix*.

Example
-----------------

Given the declarations inside module ``elementary::arithmetic::funcScalarValue``:

.. code-block:: aimms

    DeclarationSection scalar_value_global_declarations {
        Parameter p_rev;
        Parameter p_cst;
        Parameter p_pct;
        Parameter p_cap;
    }
    
Then the code:

.. code-block:: aimms

    p_rev := 12 ;
    p_cst := 34 ;
    p_pct := 56 ;
    p_cap := 78 ;
    _s_kpis := scalar_value_global_declarations ;
    _p_kpiVal(_i_kpi) := ScalarValue( _i_kpi );

    block where single_column_display := 1;
        display _p_kpiVal ;
    endblock ;

Will put the following table in the listing file:

.. code-block:: aimms

    _p_kpiVal := data 
    { 'elementary::arithmetic::funcScalarValue::p_rev' : 12,
      'elementary::arithmetic::funcScalarValue::p_cst' : 34,
      'elementary::arithmetic::funcScalarValue::p_pct' : 56,
      'elementary::arithmetic::funcScalarValue::p_cap' : 78 } ;


.. note::

    When *identifier* or *identifier.suffix* is not a scalar numerical
    valued reference, the function :aimms:func:`ScalarValue` returns 0.0.

.. seealso::

    - The function :aimms:func:`Val`. 
    - The :aimms:func:`ScalarValue` function is a function that operates on subsets of :aimms:set:`AllIdentifiers`. 
    - Other functions that operate on subsets of :aimms:set:`AllIdentifiers` are referenced in :doc:`data-communication-components/data-initialization-verification-and-control/working-with-the-set-allidentifiers` of the Language Reference.
