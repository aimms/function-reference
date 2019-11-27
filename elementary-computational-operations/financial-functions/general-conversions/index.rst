.. _chap:finance-convertingdata:

General Conversions
-------------------

.. _FF.conv:

Prices (such as security prices) are often provided as a fractional
price, whereas the financial functions in AIMMS always expect decimal
prices. AIMMS supports the following conversion functions between
fractional and decimal prices:

-  :aimms:func:`PriceDecimal`
-  :aimms:func:`PriceFractional`

Annual interest rates can be given as a nominal rate (just the sum of
interest rates over the number of compounding periods) or in the form of
an effective rate (including the effects of interest over interest for
all compounding periods). AIMMS supports the following interest rate
conversion functions:

-  :aimms:func:`RateEffective`
-  :aimms:func:`RateNominal`

.. toctree::
   :hidden:

   pricedecimal
   pricefractional
   rateeffective
   ratenominal
