.. aimms:function:: PriceDecimal(FractionalPrice, FractionBase)

.. _PriceDecimal:

PriceDecimal
============

The function :aimms:func:`PriceDecimal` converts a price expressed as a fractional
number to a price expressed as a decimal number depending on the input
parameter *FractionBase*.

.. code-block:: aimms

    PriceDecimal(
        FractionalPrice,             ! (input) numerical expression
        FractionBase                 ! (input) numerical expression
        )

Arguments
---------

    *FractionalPrice*
        The price expressed as a fractional number. *FractionalPrice* can be any
        real number.

    *FractionBase*
        The base used as the denominator of the fraction. *FractionBase* must be
        a positive integer.

Return Value
------------

    The function :aimms:func:`PriceDecimal` returns the *FractionalPrice* expressed as
    a decimal number.

Equation
--------

    The conversion between decimal and fractional prices is based on the
    system of equations

    .. math:: \begin{cases} \lfloor p_f \rfloor = \lfloor p_d \rfloor & \quad\mbox{(integer parts)}\\ p_f - \lfloor p_f \rfloor = \frac{b}{10^{\lceil \log{b}\rceil}}\left(p_d-\lfloor p_d \rfloor\right) & \quad\mbox{(fractional parts)} \end{cases}

    \ where :math:`p_d` is the decimal price, :math:`p_f` the fractional
    price and :math:`b` the base.

.. note::

    -  For bases which are a power of 10, the decimal and fractional prices
       coincide. In all other cases, the fractional price is smaller than
       the decimal price.

    -  The function :aimms:func:`PriceDecimal` is similar to the Excel function
       `DOLLARDE <https://support.microsoft.com/en-us/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427>`_ .


Example
--------

.. code-block:: aimms

    _p_r1 := PriceDecimal( 1.02, 16 );
    _p_r2 := PriceDecimal( 1.1 , 32 );
    
results in:

.. code-block:: aimms

    _p_r1 := 1.125000 ;
    _p_r2 := 1.312500 ;

.. seealso::

    *   The function :aimms:func:`PriceFractional`.

    *   `Microsoft support DOLLARDE <https://support.microsoft.com/en-us/office/dollarde-function-db85aab0-1677-428a-9dfd-a38476693427>`_.

    *   `EXCELJET example DOLLARDE <https://exceljet.net/functions/dollarde-function>`_.