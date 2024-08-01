.. aimms:function:: RateNominal(EffectiveRate, NumberPeriods)

.. _RateNominal:

RateNominal
===========

The function :aimms:func:`RateNominal` returns the nominal annual interest rate,
expressed as a fraction, on the basis of an effective annual interest
rate plus the number of compounding periods per year.

.. code-block:: aimms

    RateNominal(
        EffectiveRate,             ! (input) numerical expression
        NumberPeriods              ! (input) numerical expression
        )

Arguments
---------

    *EffectiveRate*
        The effective annual interest rate expressed as a fraction.
        *EffectiveRate* must be a nonnegative decimal number.

    *NumberPeriods*
        The number of compounding periods per year. *NumberPeriods* must be a
        positive integer.

Return Value
------------

    The function :aimms:func:`RateNominal` returns the nominal annual interest rate
    expressed as a fraction.

.. note::

    -  The equation on which the conversion between nominal and effective
       rates is based, is explained for the function :aimms:func:`RateEffective` (the inverse
       of :aimms:func:`RateNominal`).

    -  This function can be used in an objective function or constraint, and
       the input parameter *EffectiveRate* can be used as a variable.

    -  The function :aimms:func:`RateNominal` is similar to the Excel function
       ``NOMINAL``.

Example
--------

.. code-block:: aimms

	_p_r1 := RateNominal( 2, 12 );  
	_p_r2 := RateNominal( 5, 12 ); 

	block where listing_number_precision := 6 ;
		display _p_r1, _p_r2 ;
	endblock ;
    
results in:

.. code-block:: aimms

    _p_r1 := 1.150472 ;
    _p_r2 := 1.932440 ;

References
-----------

    *   The function :aimms:func:`RateEffective`.

    *   `Microsoft Support EXCEL Nominal <https://support.microsoft.com/en-us/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b>`_

	
