.. aimms:function:: PriceFractional(DecimalPrice, FractionBase)

.. _PriceFractional:

PriceFractional
===============

The function :aimms:func:`PriceFractional` converts a price expressed as a decimal
number to a price expressed as a fractional number depending on the
input parameter *FractionBase*.

.. code-block:: aimms

    PriceFractional(
        DecimalPrice,             ! (input) numerical expression
        FractionBase              ! (input) numerical expression
        )

Arguments
---------

    *DecimalPrice*
        The price expressed as a decimal number. *DecimalPrice* can be any real
        number.

    *FractionBase*
        The base to be used as the denominator of the fraction. *FractionBase*
        must be a positive integer.

Return Value
------------

    The function :aimms:func:`PriceFractional` returns the *DecimalPrice* expressed as
    a fractional number.

.. note::

    -  The system of equations on which the conversion between decimal and
       fractional prices is based, is explained for the function :aimms:func:`PriceDecimal`
       (the inverse of :aimms:func:`PriceFractional`).

    -  The function ``FractionalDecimal`` is similar to the Excel function
       ``DOLLARFR``.


Example
--------

.. code-block:: aimms

	_p_r1 := PriceFractional( 1.125000, 16 );
	_p_r2 := PriceFractional( 1.312500, 32 );

	block where listing_number_precision := 6 ;
		display _p_r1, _p_r2 ;
	endblock ;
    
results in:

.. code-block:: aimms

    _p_r1 := 1.020000 ;
    _p_r2 := 1.100000 ;


.. seealso::

    *   The function :aimms:func:`PriceDecimal`.

    *   `Microsoft support DOLLARDE <https://support.microsoft.com/en-us/office/dollarfr-function-0835d163-3023-4a33-9824-3042c5d4f495>`_.

